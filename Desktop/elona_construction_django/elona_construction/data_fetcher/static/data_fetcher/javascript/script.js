jQuery(document).ready(function($){
	//open popup
	$('.cd-popup-trigger').on('click', function(event){
		event.preventDefault();
		$('.cd-popup').addClass('is-visible');
	});
	
	//close popup
	$('.cd-popup').on('click', function(event){
		if( $(event.target).is('.cd-popup-close') || $(event.target).is('.cd-popup') ) {
			event.preventDefault();
			$(this).removeClass('is-visible');
		}
	});
	//close popup when clicking the esc keyboard button
	$(document).keyup(function(event){
    	if(event.which=='img-replace27'){
    		$('.cd-popup').removeClass('is-visible');
	    }
    });

	var $signUp = $('.signUpSect');
	var $signIn = $('.signInSect');



    $(".btn-signin").click(function() {
		$signUp.fadeOut('slow');
		$signIn.fadeIn('slow');
		$('.signInSect').removeClass('hide');
		$('.signUpSect').toggleClass('hide');
	  });
	 $(".btn-signup").click(function() {
		$signIn.fadeOut('slow');
		$signUp.fadeIn('slow');
		$('.signUpSect').removeClass('hide');
		$('.signInSect').toggleClass('hide');
	  });
  

    $(document).ready(function(){
      $("button").click(function(){
          /* Set all the cells in columns with THEHEADING in the heading to red */
      columnTh = $("table th:contains('Assign')"); // Find the heading with the text THEHEADING
      columnIndex = columnTh.index() + 1; // Get the index & increment by 1 to match nth-child indexing
      $('table tr td:nth-child(' + columnIndex + ')').css("color", "#F00"); // Set all the elements with that index in a tr red
      columnTh.css("color", "#F00"); // Set the heading red too!
  });
  });
});

var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

