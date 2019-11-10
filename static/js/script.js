/* Add New Line for Recipe Ingredients */
$(document).ready(function() {
	var ingredientCount = 2;
	$("#addIngredient").click(function() {
		$(".removeIngredientDiv").show();
		if(ingredientCount > 20) {
			alert("Only 20 steps allowed");
			return false;
		}
		var newLine = $(document.createElement('div')).attr("id", 'TextBoxIngredientDiv' + ingredientCount);
		newLine.after().html('<input id="recipe_ingredient" id="recipe_ingredients" name="recipe_ingredients" type="text" class="form-control mb-2" placeholder="List one ingredient per line" required>');
		newLine.appendTo("#TextBoxIngredientDiv");
		ingredientCount++;
	});
	$("#removeIngredient").click(function() {
		console.log(ingredientCount);
		if(ingredientCount <= 0) {
			$("#removeIngredient").prop('disabled', true);
			return false;
		}
		if(ingredientCount <= 3) {
			$("#removeIngredient").hide();
		}
		ingredientCount--;
		$("#TextBoxIngredientDiv" + ingredientCount).remove();
	});
});
/* Add New Line for Recipe Instruction */
$(document).ready(function() {
	var instructionCount = 2;
	$("#addInstruction").click(function() {
		$(".removeInstructionDiv").show();
		if(instructionCount > 15) {
			alert("Only 15 steps allowed");
			return false;
		}
		var newLineInstruction = $(document.createElement('div')).attr("id", 'TextBoxInstructionDiv' + instructionCount);
		newLineInstruction.after().html('<textarea class="form-control mb-2" id="recipe_instruction" name="recipe_instruction" type="text" placeholder="List direction one per line"></textarea required>');
		newLineInstruction.appendTo("#TextBoxInstructionDiv");
		instructionCount++;
	});
	$("#removeInstruction").click(function() {
		console.log(instructionCount);
		if(instructionCount <= 0) {
			$("#removeInstruction").prop('disabled', true);
			return false;
		}
		if(instructionCount <= 3) {
			$("#removeInstruction").hide();
		}
		instructionCount--;
		$("#TextBoxInstructionDiv" + instructionCount).remove();
	});
});
/* Confirmation Window when a recipe is Deleted */
document.getElementById("deleteConfirm").addEventListener("click", function(e) {
	if(!confirm("Do you want to remove this recipe?")) {
		e.preventDefault();
	}
});

