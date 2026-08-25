"""Attention classifier used for all four PLM representations."""

import tensorflow as tf

@tf.keras.utils.register_keras_serializable(package="pLM4CPP")
class MaskedAttentionPooling(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attention_dense = tf.keras.layers.Dense(
            1, use_bias=True, name="residue_attention_score"
        )

    def call(self, inputs):
        residue_features, residue_mask = inputs
        logits = tf.squeeze(self.attention_dense(residue_features), axis=-1)
        residue_mask = tf.cast(residue_mask, logits.dtype)
        masked_logits = logits + (1.0 - residue_mask) * tf.cast(-1e4, logits.dtype)
        weights = tf.nn.softmax(masked_logits, axis=1)
        return tf.reduce_sum(
            residue_features * tf.expand_dims(weights, axis=-1), axis=1
        )

    def get_config(self):
        return super().get_config()


def build_attention_classifier(
    embedding_dimension,
    max_len=61,
    learning_rate=1e-3,
):
    residue_input = tf.keras.Input(
        shape=(max_len, embedding_dimension), dtype=tf.float16,
        name="residue_embeddings"
    )
    mask_input = tf.keras.Input(
        shape=(max_len,), dtype=tf.uint8, name="residue_mask"
    )

    x = tf.keras.layers.LayerNormalization(
        epsilon=1e-6, name="embedding_layer_norm"
    )(residue_input)
    x = tf.keras.layers.Dense(
        128, activation="gelu", name="residue_projection"
    )(x)
    x = tf.keras.layers.Dropout(0.20, name="residue_dropout")(x)
    pooled = MaskedAttentionPooling(name="masked_attention_pooling")([x, mask_input])
    x = tf.keras.layers.Dense(128, activation="gelu", name="peptide_dense_1")(pooled)
    x = tf.keras.layers.Dropout(0.30, name="peptide_dropout_1")(x)
    x = tf.keras.layers.Dense(32, activation="gelu", name="peptide_dense_2")(x)
    x = tf.keras.layers.Dropout(0.20, name="peptide_dropout_2")(x)
    output = tf.keras.layers.Dense(
        1, activation="sigmoid", dtype="float32", name="cpp_probability"
    )(x)

    model = tf.keras.Model(
        inputs=[residue_input, mask_input], outputs=output,
        name="pLM4CPP_attention_classifier"
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss=tf.keras.losses.BinaryCrossentropy(),
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name="accuracy"),
            tf.keras.metrics.AUC(name="roc_auc", curve="ROC"),
            tf.keras.metrics.AUC(name="pr_auc", curve="PR"),
        ],
    )
    return model
