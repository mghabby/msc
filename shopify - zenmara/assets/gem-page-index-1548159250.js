

        jQuery(function() {
            var $hero = jQuery('#m-1543467162889');
            var $module = jQuery('#m-1543467162889').children('.module');

            var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
            if(mode == 'dev') {
                $hero.children('.hero-link').hide();
            }

            var height = jQuery.trim($module.attr('data-height'));
            if(height == undefined || height == '') {
                $hero.attr('style', 'height: auto!important');
                jQuery(window).resize(function(){
                    $hero.attr('style', 'height: auto!important');
                });
            } else {
                $hero.removeAttr('style');
            }

            var effect = $module.attr('data-effect');
            var transition = $module.attr('data-transition');

            if(effect == 'effect-zoom') {   
                $module.parent().addClass(effect);  

                setTimeout(function() {
                    var backgroundImage = $module.parent().css('background-image');
                    var backgroundSize = $module.parent().css('background-size');
                    var backgroundPosition = $module.parent().css('background-position');
                    $module.siblings('.gf_hero-bg-wrap').css({
                        'background-image'      : 'inherit',
                        'background-size'       : 'inherit',
                        'background-position'   : 'inherit',
                        '-webkit-transition'    : 'transform ' + transition + 's ease-in-out',
                        '-moz-transition'       : 'transform ' + transition + 's ease-in-out',
                        '-ms-transition'        : 'transform ' + transition + 's ease-in-out',
                        '-o-transition'         : 'transform ' + transition + 's ease-in-out',
                        'transition'            : 'transform ' + transition + 's ease-in-out'
                    })
                    $module.siblings('.gf_hero-bg-wrap').children('.gf_hero-bg').css({
                        'background-image'      : 'inherit',
                        'background-size'       : 'inherit',
                        'background-position'   : 'inherit',
                        '-webkit-transition'    : 'transform ' + transition + 's ease-in-out',
                        '-moz-transition'       : 'transform ' + transition + 's ease-in-out',
                        '-ms-transition'        : 'transform ' + transition + 's ease-in-out',
                        '-o-transition'         : 'transform ' + transition + 's ease-in-out',
                        'transition'            : 'transform ' + transition + 's ease-in-out'
                    });
                }, 300);
            }

            if($module.attr('data-fixedMode') == '1'){
                $module.parent().attr('style', 'padding-top: 0px!important; padding-bottom: 0px!important; height: auto!important; background-image: none!important;max-width: 100%!important;');

                jQuery(window).resize(function(){
                    var backgroundImage =  $module.parent().css('background-image');
                    $module.parent().attr('style', 'padding-top: 0px!important; padding-bottom: 0px!important; height: auto!important; background-image: none!important;max-width: 100%!important;');
                });
            } else {
                $module.parent().removeAttr('style');
            }
        });
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703').children('.module');

            var sameHeightTitle = $module.data('sameheightitle'),
                collg = $module.data('collg'),
                colmd = $module.data('colmd'),
                colsm = $module.data('colsm'),
                colxs = $module.data('colxs');

            var $clearfixes = $module.find('.gf_row-no-padding').children('.gf_clearfix');
            var col = collg;


            jQuery(window).resize(function() {
                setTimeout(function() {
                    for(var i = 0; i < $clearfixes.length; i++) {
                        if($clearfixes.eq(i).css('display') == 'block') {
                            if($clearfixes.eq(i).hasClass('visible-lg')) {
                                col = collg;
                                break;
                            }
                            if($clearfixes.eq(i).hasClass('visible-md')) {
                                col = colmd;
                                break;
                            }
                            if($clearfixes.eq(i).hasClass('visible-sm')) {
                                col = colsm;
                                break;
                            }
                            if($clearfixes.eq(i).hasClass('visible-xs')) {
                                col = colxs;
                                break;
                            }
                        }
                    }
                }, 1000);
            });

            if(sameHeightTitle == '1') {
                var minHeight = 0;

                $module.find('.product-single__title').each(function() {
                });
            } else {
            }
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child1').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child1-3').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child1-1').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child1-2').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child2').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child2-3').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child2-1').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child2-2').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child3').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child3-3').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child3-1').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543468117703-child3-2').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1543478126499').children('.module');
        
            var token_test = '2269641474.1677ed0.63eaaf968720481a866e9263fc8639e1';
            var token = $module.data('token') != '' ? $module.data('token') : token_test;
            var num_photos = parseInt($module.data('photos')) > 1 ? parseInt($module.data('photos')) : 1;
            var num_columns = parseInt($module.data('columns')) > 1 ? parseInt($module.data('columns')) : num_photos;
            var padding = parseInt($module.data('padding')) > 0 ? parseInt($module.data('padding')) : 0;

            var instaTag = jQuery.trim($module.data('hashtag')) != '' ? jQuery.trim($module.data('hashtag')) : '';

            if(instaTag != '') {
                var instaUrl = 'https://api.instagram.com/v1/tags/' + instaTag + '/media/recent';
            } else {
                var instaUrl = 'https://api.instagram.com/v1/users/self/media/recent';
            }

            jQuery.ajax({
                url: instaUrl,
                dataType: 'jsonp',
                type: 'GET',
                data: {
                    access_token: token, 
                    count: num_photos
                },
                success: function(data) {
                    var html = '';
                    if(data.data != undefined) {
                        for(var i = 0; i < data.data.length; i++) {
                            if(i % num_columns == 0) {
                                html += '<div class="gf_clearfix"></div>';
                            }
                            html += '<li><a href="' + data.data[i].link + '" target="_blank" style="padding: ' + padding + 'px;">';
                                html+= '<img src="'+ data.data[i]['images'].standard_resolution.url + '" alt="' + data.data[i].caption + '" />';
                            html += '</a></li>';
                        }
                        $module.html(html).hide();
                        $module.find('li').css('width', (100/num_columns)+'%');

                        $module.closest('.module-wrap').css('marginLeft', padding * -1);
                        $module.closest('.module-wrap').css('marginRight', padding * -1);
                    }
                    $module.fadeIn();
                },
                error: function(data){  
                    console.log(data);
                }
            });
        });
    
        jQuery(function() {
            var $module = jQuery('#m-1543482115069').children('.module');
        
            var token_test = '2269641474.1677ed0.63eaaf968720481a866e9263fc8639e1';
            var token = $module.data('token') != '' ? $module.data('token') : token_test;
            var num_photos = parseInt($module.data('photos')) > 1 ? parseInt($module.data('photos')) : 1;
            var num_columns = parseInt($module.data('columns')) > 1 ? parseInt($module.data('columns')) : num_photos;
            var padding = parseInt($module.data('padding')) > 0 ? parseInt($module.data('padding')) : 0;

            var instaTag = jQuery.trim($module.data('hashtag')) != '' ? jQuery.trim($module.data('hashtag')) : '';

            if(instaTag != '') {
                var instaUrl = 'https://api.instagram.com/v1/tags/' + instaTag + '/media/recent';
            } else {
                var instaUrl = 'https://api.instagram.com/v1/users/self/media/recent';
            }

            jQuery.ajax({
                url: instaUrl,
                dataType: 'jsonp',
                type: 'GET',
                data: {
                    access_token: token, 
                    count: num_photos
                },
                success: function(data) {
                    var html = '';
                    if(data.data != undefined) {
                        for(var i = 0; i < data.data.length; i++) {
                            if(i % num_columns == 0) {
                                html += '<div class="gf_clearfix"></div>';
                            }
                            html += '<li><a href="' + data.data[i].link + '" target="_blank" style="padding: ' + padding + 'px;">';
                                html+= '<img src="'+ data.data[i]['images'].standard_resolution.url + '" alt="' + data.data[i].caption + '" />';
                            html += '</a></li>';
                        }
                        $module.html(html).hide();
                        $module.find('li').css('width', (100/num_columns)+'%');

                        $module.closest('.module-wrap').css('marginLeft', padding * -1);
                        $module.closest('.module-wrap').css('marginRight', padding * -1);
                    }
                    $module.fadeIn();
                },
                error: function(data){  
                    console.log(data);
                }
            });
        });
    
        jQuery(function() {
            var $module = jQuery('#m-1548366014715').children('.module');   
            var navspeed = $module.data('navspeed'),
                autoplaytimeout = $module.data('autoplaytimeout'),
                autoplayhoverpause = $module.data('autoplayhoverpause'),
                navlg = $module.data('navlg'),
                navmd = $module.data('navmd'),
                navsm = $module.data('navsm'),
                navxs = $module.data('navxs'),
                collg = $module.data('collg'),
                colmd = $module.data('colmd'),
                colsm = $module.data('colsm'),
                colxs = $module.data('colxs'),
                dotslg = $module.data('dotslg'),
                dotsmd = $module.data('dotsmd'),
                dotssm = $module.data('dotssm'),
                dotsxs = $module.data('dotsxs'),
                marginlg = parseInt($module.data('marginlg')),
                marginmd = parseInt($module.data('marginmd')),
                marginsm = parseInt($module.data('marginsm')),
                marginxs = parseInt($module.data('marginxs'));

            var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
            if(mode == 'production') {
                var autoplay = $module.data('autoplay'), 
                    loop = $module.data('loop');
            } else {
                var autoplay = 0, 
                    loop = 0;
            }
        
            $module.owlCarousel({
                mouseDrag: false,
                autoplayHoverPause: autoplayhoverpause,
                autoplay: autoplay,
                autoplayTimeout: autoplaytimeout,
                loop: loop,
                navSpeed: navspeed,
                autoWidth: !1,
                responsiveClass:true,
                responsive:{
                    0:{
                        items:colxs,
                        nav: navxs,
                        dots:dotsxs,
                        margin: marginxs
                    },
                    768:{
                        items:colsm,
                        nav: navsm,
                        dots:dotssm,
                        margin: marginsm
                    },
                    992:{
                        items:colmd,
                        nav: navmd,
                        dots:dotsmd,
                        margin: marginmd
                    },
                    1200:{
                        items:collg,
                        nav: navlg,
                        dots:dotslg,
                        margin: marginlg
                    }
                }
            }); 
        }); 
    