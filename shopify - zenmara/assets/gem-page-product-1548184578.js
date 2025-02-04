

        jQuery(function() {
            var $module = jQuery('#m-1539774978372').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978308').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978314').children('.module');
            $module.gfV3ProductImageList({
                onImageClicked: function(imageUrl, imageZoomUrl) {}
            });

            var style = $module.attr('data-style');
            switch(style) {
                case 'slider':
                    var navspeed = $module.data('navspeed'),
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

                        marginlg = parseInt($module.data('mlg')),
                        marginmd = parseInt($module.data('mmd')),
                        marginsm = parseInt($module.data('msm')),
                        marginxs = parseInt($module.data('mxs'));

                    var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                    if(mode == 'production') {
                        var loop = $module.data('loop');
                    } else {
                        var loop = 0;
                    }
                    $module.find('.gf_product-images-list').owlCarousel({
                        mouseDrag: true,
                        navSpeed: navspeed,
                        autoWidth: !1,
                        loo: loop,
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
                    break;
            }
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978347').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978300').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
          var $module = jQuery('#m-1548194035131').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1548194759367').children('.module');
            var swatchText = $module.attr('data-swatch-text') != undefined ? $module.attr('data-swatch-text') : '1';
            $module.gfV3ProductSwatches({
                swatchText: swatchText,
                onSwatchSelected: function(variant, $swatch) {}
            });
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978355').children('.module');
            var style = $module.attr('data-style');
            var updatePrice = $module.attr('data-updateprice');

            $module.gfV3ProductQuantity({
                'style': style,
                'updatePrice': updatePrice
            });
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1548186215695').children('.module');
            $module.gfV1StockCounter();
        });
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978344').children('.module');
            $module.gfV3ProductCartButton({ onItemAdded: function() {}});
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978302').children('.module');
            $module.gfV1Countdown({
                id: "1539774978302",
                idSlug: "1539774978302"
            });
        });
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978278').children('.module');
            $module.gfV3ProductDesc();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978364').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247').children('.module');

            var limit = parseInt($module.attr('data-limit'));
            if($module.find('.gf_row.gf_row_no_tools .gf_column').length > limit) {
                $module.find('.gf_row.gf_row_no_tools .gf_column:last').hide();
            }
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child1').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child1-4').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child1-6').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child1-5').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child2').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child2-4').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child2-6').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child2-5').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child3').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child3-4').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child3-6').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child3-5').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child4').children('.module');
            $module.gfV3Product();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child4-4').children('.module');
            var effect = $module.attr('data-effect');
            $module.gfV3ProductImage({
                'effect': effect
            })
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child4-6').children('.module');
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1539774978247-child4-5').children('.module');
            $module.gfV3ProductPrice();
        }); 
    
        jQuery(function() {
            var $module = jQuery('#m-1548196690520').children('.module');   
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
    
        jQuery(function() {
          var $module = jQuery('#m-1548196690531').children('.module');
        }); 
    