var CLOUDINARY_URL = 'https://api.cloudinary.com/v1_1/dbnahdjbc/upload';
var CLOUDINARY_UPLOAD_PRESET = 'trhi3mfq';

var imgPreview = document.getElementById('img-preview');
var recipe_image = document.getElementById('file-upload');

recipe_image.addEventListener('change', function(event) {
    var file = event.target.files[0];
    var formData = new FormData();
    formData.append('file', file);
    formData.append('upload_preset', CLOUDINARY_UPLOAD_PRESET);

    axios({
        url: CLOUDINARY_URL,
        method: 'POST',
        header: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: formData
    }).then(function(res) {
        console.log(res);
        imgPreview.src = res.data.secure_url;
    }).catch(function(err) {
        console.error("Please choose an other image")
    });
});


