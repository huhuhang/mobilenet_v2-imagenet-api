<div align="center">
  <h1>ImageNet Predict</h1>
  <b>MOBILENET V2 IMAGENET API</b>
</div>

<br />

## Usage

<pre>curl -X <b>POST</b> -F image=@image.jpg 'https://mobilenet-v2-imagenet.herokuapp.com/predict'</pre>

```json
{
  "predictions": [
    { "label": "sports_car", "probability": 0.855 },
    { "label": "racer", "probability": 0.028 },
    { "label": "convertible", "probability": 0.022 },
    { "label": "grille", "probability": 0.014 },
    { "label": "car_wheel", "probability": 0.009 }
  ],
  "success": true
}
```