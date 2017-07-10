			var wode = document.getElementById("wode");
			var wo = document.getElementById("wo");		
				wo.onmouseover=function(){
					wode.style.display = "block";
					wo.className="hi"
					wode.onmouseover=function(){
						wo.className="hi"
						this.style.display = "block";
					}
				}
				wo.onmouseout=function() {
					wode.style.display = "none";
					wo.className=""	
					wode.onmouseout=function(){
						this.style.display = "none";
						wo.className=""
					}
			     }

			var guanzhu = document.getElementById("guanzhu");
			var guan = document.getElementById("guan");		
				guan.onmouseover=function(){
					guanzhu.style.display = "block";
					guan.className="hi"
					guanzhu.onmouseover=function(){
						guan.className="hi"
						this.style.display = "block";
					}
				}
				guan.onmouseout=function() {
					guanzhu.style.display = "none";
					guan.className=""	
					guanzhu.onmouseout=function(){
						this.style.display = "none";
						guan.className=""
					}
			     }

			var kefu = document.getElementById("kefu");
			var ke = document.getElementById("ke");		
				ke.onmouseover=function(){
					kefu.style.display = "block";
					ke.className="hi"
					kefu.onmouseover=function(){
						ke.className="hi"
						this.style.display = "block";
					}
				}
				ke.onmouseout=function() {
					kefu.style.display = "none";
					ke.className=""	
					kefu.onmouseout=function(){
						this.style.display = "none";
						ke.className=""
					}
			     }

			var daohang = document.getElementById("daohang");
			var dao = document.getElementById("dao");		
				dao.onmouseover=function(){
					daohang.style.display = "block";
					dao.className="hi"
					daohang.onmouseover=function(){
						dao.className="hi"
						this.style.display = "block";
					}
				}
				dao.onmouseout=function() {
					daohang.style.display = "none";
					dao.className=""	
					daohang.onmouseout=function(){
						this.style.display = "none";
						dao.className=""
					}
			     }



			var ready = document.getElementById("ready");
			var readyy = document.getElementById("readyy");		
				readyy.onmouseover=function(){
					ready.style.display = "block";
					readyy.className="hi"
					ready.onmouseover=function(){
						readyy.className="hi"
						this.style.display = "block";
					}
				}
				readyy.onmouseout=function() {
					ready.style.display = "none";
					readyy.className=""	
					ready.onmouseout=function(){
						this.style.display = "none";
						readyy.className=""
					}
			     }


			var shopping = document.getElementById("shopping");
			var down = document.getElementById("shopping-down");		
				shopping.onclick=function(ev){
					var oEven=ev||event;
				  down.style.display = "block";
				  oEven.cancelBubble=true;
				
				}
				document.onclick=function(){
					down.style.display = "none";
				}



		$(function() {
			var bannerSlider = new Slider($('#banner_tabs'), {
				time: 3000,
				delay: 400,
				event: 'hover',
				auto: true,
				mode: 'fade',
				controller: $('#bannerCtrl'),
				activeControllerCls: 'active'
			});
			$('#banner_tabs .flex-prev').click(function() {
				bannerSlider.prev()
			});
			$('#banner_tabs .flex-next').click(function() {
				bannerSlider.next()
			});
		})