$(document).ready(function () {
    var ingredientCounter = 2;
    $("#addIngredient").click(function () {
        $(".removeIngredient").show();
        
        if(ingredientCounter > 15) {
            alert("Max of 15 ingredients allowed");
            return false
        }
        
        var newTextBox = $(document.createElement('div'))
            .attr("class", 'col-10 mt-2')
            .attr("id", 'TextBoxIngredient' + ingredientCounter)
            
        newTextBox.after().html(
            '<input type="text" name="instruction" id="recipe_instruction" value "" required class="form-control"/>'
        );
            
        newTextBox.appendTo("#TextBoxIngredient");
        ingredientCounter++;
    });
    
    $("#removeIngredient").click(function () {
        if(ingredientCounter <= 1) {
            $("#removeIngredient").prop('disable', True);
            return false
        }    
    
        ingredientCounter--;
        $("#TextBoxIngredient" + ingredientCounter).remove();
    });
    
})