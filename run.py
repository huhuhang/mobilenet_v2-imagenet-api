# 请求方法
# curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'

import tensorflow as tf
from PIL import Image
import numpy as np
import flask
import io

# 初始化 Flask 应用和模型
app = flask.Flask(__name__)
model = None

def load_model():
	# 加载预训练模型
	global model
	model = tf.keras.applications.MobileNetV2(weights="imagenet")

def prepare_image(image, target):
	# 转换图片为 RGB 编码
	if image.mode != "RGB":
		image = image.convert("RGB")
	# 预处理图片为模型可接受格式
	image = image.resize(target)
	image = tf.keras.preprocessing.image.img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

	return image

@app.route('/')
def index():
    return 'Please use the POST method to get predictions.'

@app.route("/predict", methods=["POST"])
def predict():
	load_model() # 提前加载模型
	data = {"success": False}
	if flask.request.method == "POST":
		if flask.request.files.get("image"):
			# 读取图片为 PIL 格式
			image = flask.request.files["image"].read()
			image = Image.open(io.BytesIO(image))
			# 预处理图片
			image = prepare_image(image, target=(224, 224))
			# 推理
			graph = tf.get_default_graph()
			with graph.as_default():
				preds = model.predict(image)
			# 使用 ImageNet 标签对推理结果进行解码
			results = tf.keras.applications.mobilenet_v2.decode_predictions(preds)
			# 确定返回 JSON 格式
			data["predictions"] = []
			for (imagenetID, label, prob) in results[0]:
				r = {"label": label, "probability": float(prob)}
				data["predictions"].append(r)
			data["success"] = True

	return flask.jsonify(data)

# 启动
if __name__ == "__main__":
	app.run(host='127.0.0.1', debug=True)