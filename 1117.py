try:
    import tensorflow as tf
    print("TensorFlow 版本:", tf.__version__)
    from tensorflow import keras
    print("Keras 成功導入！")
except ImportError as e:
    print("模組未安裝:", e)
