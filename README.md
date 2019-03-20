<div align="center">
  <h1>ImageNet Inference</h1>
  <b>MOBILENET V2 IMAGENET API</b>
</div>

<br />

## Usage

Run `python run.py` locally to start the Flask web service:

<pre>curl -X <b>POST</b> -F image=@test.jpg 'http://127.0.0.1:5000/predict'</pre>

Or use the Heroku API:

<pre>curl -X <b>POST</b> -F image=@test.jpg 'https://mobilenet-v2-imagenet.herokuapp.com/predict'</pre>


```json
{
  "predictions": [
    { "label": "sports_car", "probability": 0.856 },
    { "label": "racer", "probability": 0.028 },
    { "label": "convertible", "probability": 0.022 },
    { "label": "grille", "probability": 0.014 },
    { "label": "car_wheel", "probability": 0.009 }
  ],
  "status": "success"
}
```