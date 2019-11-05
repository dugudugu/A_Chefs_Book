 $(document).ready(function () {
            // ingredients
            var ingredientCount = 2;
            $("#addIngredient").click(function () {
                $(".removeIngredientDiv").show();
                if (ingredientCount > 20) {
                    alert("Only 20 steps allowed");
                    return false;
                }
                
                var newLine = $(document.createElement('div'))
                    .attr("id", 'TextBoxIngredientDiv' + ingredientCount);
                    
                newLine.after().html(
                    '<input id="recipe_ingredient" id="recipe_ingredients" name="recipe_ingredients" type="text" placeholder="extra ingredient"class="form-control">'
                    );
               newLine.appendTo("#TextBoxIngredientDiv");
               ingredientCount++;
            });
            $("#removeIngredient").click(function () {
                console.log(ingredientCount)
                if (ingredientCount <= 1) {
                    $("#removeIngredient").prop('disabled', true);
                    return false;
                }
                if (ingredientCount <= 3) {
                    $("#removeIngredient").hide();
                }
                ingredientCount--;
                $("#TextBoxIngredientDiv" + ingredientCount).remove();
            });
        });