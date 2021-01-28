$(document).ready(function(){
	
	
	$('.img_popup').magnificPopup({
		type: 'image',
		gallery: {
				enabled: true
			}
	});
	
	/* Isotope Active */
		$(".gallery_area").imagesLoaded(function () {
			var grid = $(".grid").isotope({
				itemSelector: ".grid-item",
				percentPosition: true,
				masonry: {
					columnWidth: ".grid-item"
				}
			});

			$(".gallery_list").on("click", "li", function () {
				var filterValue = $(this).attr("data-filter");
				grid.isotope({
					filter: filterValue
				});
			});
			/* Isotope Menu Active
			============================*/
			$(".gallery_list li").on("click", function (event) {
				$(this)
					.siblings(".active")
					.removeClass("active");
				$(this).addClass("active");
				event.preventDefault();
			});
		});
	
		
		/* counter Up */
		$('.counter').counterUp({
				delay: 10,
				time: 1000
					});
	
});


$(document).ready(function(){
	
 $(".header_right ul li").click(function(){
    $(".header_right ul li ul ").toggle();
})

	

});

	//Sticky Header
  $(window).on('scroll',function() {    
   var scroll = $(window).scrollTop();
   if (scroll < 20) {
    $(".sticky").removeClass("scroll-header");
   }else{
    $(".sticky").addClass("scroll-header");
   }
  }); 
  
 
	
	