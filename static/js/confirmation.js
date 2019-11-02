document.getElementById("deleteConfirm").addEventListener("click", function(e){
    if (! confirm("Do you want to remove this recipe?")) {
        e.preventDefault();
    }
})