
jQuery(document).ready(function($) {

	"use strict";

	[].slice.call( document.querySelectorAll( 'select.cs-select' ) ).forEach( function(el) {
		new SelectFx(el);
	});

	jQuery('.selectpicker').selectpicker;
	
	function selectMac(em){
		const macAddress = em.text();
		
		$('#MAC').val(macAddress);
		$('#dropDownMac').empty()
		$('#dropDownMac').hide()
	}

	$('#submitBtn').click(function(){
		$.ajax({
			url: 'http://localhost:8000/wifi/date/',
			data: {
				't1': $('#form_date1').val(),
				't2': $('#form_date2').val(),
				'macAddr': $('#MAC').val()
			},
			type: 'POST',
			success: function (res) {
				console.log(res)
			},
			error: function (error) {
					console.log(error);
			}
	});
	})

	$('#checkMac').click(function(){
		$.ajax({
				url: 'http://localhost:8000/wifi/maclist/',
				data: {
					'user_name': $('#user_name').val()
				},
				type: 'POST',
				success: function (res) {
					$('#dropDownMac').empty()
					for(var i=0; i<res.length; i++) {
						
						const dropdownItemElement = $(document.createElement('a'));
						dropdownItemElement.click(() => {
							selectMac(dropdownItemElement);
						});
						dropdownItemElement.addClass("dropdown-item");
						dropdownItemElement.text(res[i]['device_mac']);
						
						$('#dropDownMac').append(dropdownItemElement);
					}
					$('#dropDownMac').show()
				},
				error: function (error) {
						console.log(error);
				}
		});
	})



	$('#form_date1').datetimepicker({
	  language:  'ko',
	  weekStart: 1,
	  todayBtn:  1,
	  autoclose: 1,
	  todayHighlight: 1,
	  startView: 2,
	  minView: 2,
	  forceParse: 0
	});

	$('#form_date2').datetimepicker({
	  language:  'ko',
	  weekStart: 1,
	  todayBtn:  1,
	  autoclose: 1,
	  todayHighlight: 1,
	  startView: 2,
	  minView: 2,
	  forceParse: 0
	});


	$('.search-trigger').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').addClass('open');
	});

	$('.search-close').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').removeClass('open');
	});

	$('.equal-height').matchHeight({
		property: 'max-height'
	});

	// var chartsheight = $('.flotRealtime2').height();
	// $('.traffic-chart').css('height', chartsheight-122);


	// Counter Number
	$('.count').each(function () {
		$(this).prop('Counter',0).animate({
			Counter: $(this).text()
		}, {
			duration: 3000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});




	// Menu Trigger
	$('#menuToggle').on('click', function(event) {
		var windowWidth = $(window).width();
		if (windowWidth<1010) {
			$('body').removeClass('open');
			if (windowWidth<760){
				$('#left-panel').slideToggle();
			} else {
				$('#left-panel').toggleClass('open-menu');
			}
		} else {
			$('body').toggleClass('open');
			$('#left-panel').removeClass('open-menu');
		}

	});


	$(".menu-item-has-children.dropdown").each(function() {
		$(this).on('click', function() {
			var $temp_text = $(this).children('.dropdown-toggle').html();
			$(this).children('.sub-menu').prepend('<li class="subtitle">' + $temp_text + '</li>');
		});
	});


	// Load Resize
	$(window).on("load resize", function(event) {
		var windowWidth = $(window).width();
		if (windowWidth<1010) {
			$('body').addClass('small-device');
		} else {
			$('body').removeClass('small-device');
		}

	});


});
