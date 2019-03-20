<div align="center">
  <h1>ImageNet Predict</h1>
  <b>MOBILENET V2 IMAGENET API</b>
</div>

<br />

## Usage

<pre>curl -X <b>POST</b> -F image=@image.jpg 'https://mobilenet-v2-imagenet.herokuapp.com/predict'</pre>

```json
{
  "species": "dog",
  "url": "https://images.dog.ceo/breeds/saluki/n02091831_3242.jpg"
}
```