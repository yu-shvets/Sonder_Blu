$(function () {
	$('.vase').not('.vase-one').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$('.vase').not($(this)).removeClass('active');
		if (!$(this).hasClass('active')) {
			$(this).addClass('active');
			$('.sidebar-cards').addClass('show');
		}
		else{
			$(this).removeClass('active');
			$('.sidebar-cards').removeClass('show');
		}
	});
	$('.vase-one').not('.vase-two').click(function(event) {
		/* Act on the event */
		// $('.vase-one').not($(this)).removeClass('active');
		if (!$(this).hasClass('active')) {
			$(this).addClass('active');
			$(this).parents('.searchWrap-content__box').find('.vid').hide();
			$(this).parents('.searchWrap-content__box').find('.slider-video').show();
			$(this).parents('.searchWrap-content__box').find('.slider-video').addClass('slider');
			$(this).parents('.searchWrap-content__box').find('.slider-video.slider').slick({
				dots: true,
				arrows: false,
				slidesToShow: 1
			});
		}
		else{
			$(this).removeClass('active');
			$(this).parents('.searchWrap-content__box').find('.vid').show();
			$(this).parents('.searchWrap-content__box').find('.slider-video').hide();
			$(this).parents('.searchWrap-content__box').find('.slider-video').removeClass('slider');
			$(this).parents('.searchWrap-content__box').find('.slider-video').slick('unslick');
		}
	});
	$('.slider-video.slider').slick({
		dots: true,
		arrows: false,
		slidesToShow: 1
	});
	$(".sidebar-friends__box").mCustomScrollbar();
	$('.videoWrap iframe').click();
	$('.sidebar-cards__item a').hover(function() {
		/* Stuff to do when the mouse enters the element */
		var data = $(this).data('video');
		// alert(data);
		$('.videoWrap iframe').attr({
			'src': data
		});
	}, function() {
		/* Stuff to do when the mouse leaves the element */
	});
	$('.sliderWrap').slick({
		dots: true,
		arrows: false,
		slidesToShow: 1
	});
	$('.accordion-title').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$(this).closest('.accordion-wrap').find('.accordion-box').slideToggle(200);
	});
	$('.open-chat').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$(this).parent('.content').toggleClass('open-chat-box');
		$(this).parent('.content').find('.content-rgt').toggle();
		$(this).parents('body').toggleClass('chat-open');
	});
	$('.hide-sidebar').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		$(this).parents('body').toggleClass('sidebar-close');
		$(this).parents('body').find('.sidebar').toggleClass('hide');
	});
	$('.searchWrap-tabs__item input').change(function(event) {
		/* Act on the event */
		if ($(this).data('tabs') == 2) {
			$('.searchWrap-filter').addClass('active');
		}else{
			$('.searchWrap-filter').removeClass('active');
		}
		$('.searchWrap-content').removeClass('active');
		$('.searchWrap-content[data-content="'+$(this).data('tabs')+'"]').addClass('active');
	});
	$(".demo").TimeCircles({
		start: true, // determines whether or not TimeCircles should start immediately.
			animation: "smooth", // smooth or ticks. The way the circles animate can be either a constant gradual rotating, slowly moving from one second to the other. 
			count_past_zero: false, // This option is only really useful for when counting down. What it does is either give you the option to stop the timer, or start counting up after you've hit the predefined date (or your stopwatch hits zero).
			circle_bg_color: "#959595", // determines the color of the background circle.
			use_background: true, // sets whether any background circle should be drawn at all. 
			fg_width: 0.012, //  sets the width of the foreground circle. 
			bg_width: 1.2,// sets the width of the backgroundground circle. 
			text_size: 0.07, // This option sets the font size of the text in the circles. 
			total_duration: "Auto", // This option can be set to change how much time will fill the largest visible circle.
			direction: "Clockwise", // "Clockwise", "Counter-clockwise" or "Both".
			use_top_frame: false,
			start_angle: 2, // This option can be set to change the starting point from which the circles will fill up. 
			time: { //  a group of options that allows you to control the options of each time unit independently.
			Days: {
			show: false,
			text: "Days",
			color: "#FC6"
			},
			Hours: {
			show: false,
			text: "Hours",
			color: "#9CF"
			},
			Minutes: {
			show: false,
			text: "Minutes",
			color: "#BFB"
			},
			Seconds: {
			show: true,
			text: "",
			color: "#00b7f4"
			}
		}
	});
	$('canvas').attr({
		"width": '336px',
		"height": '336px'
	});;

});