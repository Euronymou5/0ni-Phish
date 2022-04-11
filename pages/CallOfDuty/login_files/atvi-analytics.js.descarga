var ATVI = ATVI || {};

(function($) {

ATVI.utils = {
	getCookies: (function() {
		var map;
		return function(update) {
			if(!map || update) {
				map = {};
				var i, cookies = document.cookie.split(";");
				for (i = 0; i < cookies.length; i++) {
					var index = cookies[i].indexOf('=');
					var x = cookies[i].substr(0, index);
					var y = cookies[i].substr(index + 1);
					x = x.replace(/^\s+|\s+$/g, '');
					if(x) map[x] = unescape(y);
				}
			}
			return map;
		};
	})(),
	
	getCookie: function(name, update) {
		return this.getCookies(update)[name];
	},
	
	setCookie: function(name, value, expireDate, path) {
		var value = escape(value);
		if(expireDate) value += '; expires=' + expireDate.toUTCString();
		value += "; path=" + (path || "/");
		document.cookie = name + '=' + value;
	},
	
	decodeBase64: function(input) {
		var charMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

		var ret = "";

		var in1, in2, in3, in4, out1, out1, out3;
		
		input = input.replace(/[^a-zA-Z0-9\+\/\=]/g, "");
		var i = 0;
		do {
			in1 = charMap.indexOf(input.charAt(i++) || "=");
			in2 = charMap.indexOf(input.charAt(i++) || "=");
			in3 = charMap.indexOf(input.charAt(i++) || "=");
			in4 = charMap.indexOf(input.charAt(i++) || "=");

			out1 = (in1 << 2) | (in2 >> 4);
			out2 = ((in2 & 15) << 4) | (in3 >> 2);
			out3 = ((in3 & 3) << 6) | in4;

			ret = ret + String.fromCharCode(out1);
			if (in3 != 64) ret = ret + String.fromCharCode(out2);
			if (in4 != 64) ret = ret + String.fromCharCode(out3);

		} while (i < input.length);
		
		return ret;

	},
	
	devHosts: ["localhost", "preview.", "uat.", "www-uat.", "cms-uat."],
		
	isProdSite: function() {
		var h = window.location.hostname;
		for(var i in this.devHosts) {
			if(h.indexOf(this.devHosts[i]) == 0) return false;
		}
		return true;
	}
};

ATVI.analytics = {
	
	ns_site: "activision",
	
	init: function() {
		this.setupPageLoad();
		this.setupClickHandlers($("body"));
	},
	
	setupClickHandlers: function(root) {
		root = $(root);
		this.setupTaggedElements(root);
		this.setupLinks(root);
	},
	
	// override as needed per site
	getSiteData: function() {
		var locPathname = window.location.pathname.replace(/\./g, '_').replace(/^\/+/, '').replace(/\/+/g, '.');
		var parts = locPathname.split('.');
		if(parts[0] == "sso") parts.shift();
		
		var sitename = parts.shift();
		
		if(parts.length < 1) parts.push("login");
		parts = parts.join(".");
		
		var csSection = sitename + ".sso";
		var csSubSection = csSection + "." + parts;
		var csName = csSubSection;
		var csCtitle = csName;
		var csCtype = parts;

		return {
			csName: csName,
			csSection: csSection,
			csSubSection: csSubSection,
			csCtitle: csCtitle,
			csCtype: csCtype,
			sitename: sitename
		};
		
		//site = <site name> (ex. elite, skylanders, bond, etc.)
		//section = <site>.sso (ex. elite.sso, skylanders.sso, etc.)
		//sub_section = <site>.sso.<sso-section> (ex. elite.sso.login, skylanders.sso.resetpassword, etc.)
		//Name = exact same value as sub_section

	},
	
	setupPageLoad: function() {
		var cookies = ATVI.utils.getCookies();
		var instr = {};
		if(cookies.ATVI_INSTRUMENT) {
			try {
				instr = JSON.parse(cookies.ATVI_INSTRUMENT);
			} catch(e) {
				instr = {};
			}
		}
		
		var siteData = this.getSiteData();
		
		var prevPage = instr.page;
		instr.page = siteData.csName;
		
		var pageData = {
			site: siteData.sitename,
			lang: cookies.ACT_SSO_LOCALE || "en_US",
			name: siteData.csName,
			previous_page: prevPage,
			c_type: siteData.csCtype,
			c_title: siteData.csCtitle,
			section: siteData.csSection,
			sub_section: siteData.csSubSection
		};
		
		var eventCookie = cookies.ACT_SSO_EVENT;
		if(eventCookie) {
			eventCookie = eventCookie.replace(/^\"(.*)\"$/, "$1");
			if(instr.event != eventCookie) {
				instr.event = eventCookie;
				eventCookie = eventCookie.split(":");
				if(eventCookie[0])
					pageData.sso_event = eventCookie[0];
			}
		}
			
		//ATVI.utils.setCookie("ATVI_INSTRUMENT", JSON.stringify(instr));
		
		// special handling for specific pages
		if (pageData.c_type == "redeemCode") { // On redeem code page
			pageData.redeem_code_status = "code not yet submitted";
			
			var error = $(".sso-message");
			if (error.length > 0) {
				pageData.redeem_code_status = "error: " + error.data("error-code");
			}	
			
			var success = $("#redeem-code-success-header");
			if (success.length > 0) {
				pageData.redeem_code_status = "success";
			} 	
			if (atvi_analytics_properties) {  // what if there are empty values TODO: 
					for(var atvi_analytics_property in atvi_analytics_properties) {
						if (atvi_analytics_properties[atvi_analytics_property] != null && atvi_analytics_properties[atvi_analytics_property].length > 0) {
							pageData[atvi_analytics_property] = atvi_analytics_properties[atvi_analytics_property];
						} 
					}
					
					if ((pageData.redeem_code_country || "").match ("IT|FR|UK|DE|DK|BE|ES|PT")) {
						pageData.redeem_code_region = "EU"; 
					}
			}
			
		
			//} // Doesn't matter anymore
			
		}
		
		//this.sendData(pageData);
	},
	
	setupTaggedElements: function(root) {
		var self = this;
		
		var dataFunction = function(code, dedupe) {
			return function() {
				if(dedupe) {
					if(dedupe.last && dedupe.last == this)
						return;
					dedupe.last = this;
				}
				
				var classes = this.className.split(/\s+/);
				var className;
				
				for(i in classes) {
					if(classes[i].indexOf("atvi-instrument-") >= 0) {
						className = classes[i];
	                    className = className.substring("atvi-instrument-".length);
						break;
					}
				}
				
				if(className) {
					
					var data = {
							action_type: code + className,
							action_details: this.id,
							ns_type: "hidden"
					};
					
					switch(this.id) {
					case "login-button":
					case "remember-me-checkbox":
						data.remember_me = "" + $("#remember-me-checkbox").val();
						break;
					case "register-button":
						break;
					case "opt-out-button":
						var detailsStr = "";
                        var label;
                        var checkboxes = $('.opt-out.data-row.checkbox input[type="checkbox"]');  
                        checkboxes.each(function () {
	                       $this = $(this);  
	                       if($this.is(":checked")) {
                              label = ($this.attr("id") == "globalOptOut" ? "global-opt-out" : $this.attr("value")+"__email");
                              detailsStr += (detailsStr=="" ? label : "," + label);
	                       }          
                        });
						data.action_details = detailsStr;
						break;
					case "subscriptions-preferences-button":
						var detailsStr = "";
                        var label;
                        var checkboxList = $('.notification-class-checkbox-list');  
                        checkboxList.each(function () {
	                       $this = $(this);  
	                       if($this.find('input[type="checkbox"]').is(":checked")) {
                              label = $this.find('input[type="checkbox"]').attr("value");
                              detailsStr += (detailsStr=="" ? label : "," + label);
	                       }          
                        });
                        // select the global opt-out checkbox (this is copied from the opt-out page)
                        var checkboxes = $('.opt-out.data-row.checkbox input[type="checkbox"]');  
                        checkboxes.each(function () {
	                       $this = $(this);  
	                       if($this.is(":checked")) {
                              label = "global-opt-out";
                              detailsStr += (detailsStr=="" ? label : "," + label);
	                       }          
                        });
						data.action_details = detailsStr;
						break;
					case "":
						break;
					}
						
					//self.sendData(data);
				}
			};
		};
		
		var focusDedupe = {};
		root.find(".atvi-instrument").click(dataFunction("sso."));
		root.find(".atvi-focus-instrument").focus(dataFunction("sso.focus.", focusDedupe));
	},
	
	setupLinks: function(root) {
		var self = this;
		
		root.find("a").not(".atvi-instrument").click(function() {

			var href = this.href;
			
			var $this = $(this);
					
			var data = {
					action_type: "atvi-anchor",
					href: href,
					ns_type: "hidden"
			};
			
			var detail = "";
			if(this.id) detail += this.id + ": ";
			var linkText = $this.text().substring(0, 30);
			if(linkText.length >= 30) linkText += "...";
			detail += linkText;
			data.action_details = detail;
			
			//self.sendData(data);
			
		});
	},
	
	/*sendData: function (data) {
		
		var loc = 'http' + (document.location.href.charAt(4) == 's' ? 's://sb' : '://b') + '.scorecardresearch.com/p?c1=2&c2=14880931';
		
		// common values
		data.visitorID = this.getVisitorId();
		data.anonVisitorID = this.getAnonVisitorId();
		data.ns__t = "" + new Date().getTime();
		data.ns_c = document.characterSet || document.defaultCharset || "";
		data.c8 = document.title;
		data.c7 = document.location.href || document.URL;
		data.c9 = document.referrer;
		
		if(ATVI.uxTest && ATVI.uxTest.campaigns) {
            var campaigns = ATVI.uxTest.campaigns;
            var campaignNames = [], campaignIds = [];
            var recipeNames = [], recipeIds = [];
            var offerNames = [], offerIds = [];
            var mboxNames = [];
            for(var i = 0; i < campaigns.length; i++) {
                campaignNames.push(campaigns[i].campaignName);
                campaignIds.push(campaigns[i].campaignId);
                recipeNames.push(campaigns[i].recipeName);
                recipeIds.push(campaigns[i].recipeId);
                offerNames.push(campaigns[i].offerName);
                offerIds.push(campaigns[i].offerId);
                mboxNames.push(campaigns[i].mboxName);
            }
            data.campaignName = campaignNames.join(",");
            data.campaignId = campaignIds.join(",");
            data.recipeName = recipeNames.join(",");
            data.recipeId = recipeIds.join(",");
            data.offerName = offerNames.join(",");
            data.offerId = offerIds.join(",");
            data.mboxName = mboxNames.join(",");
        }
		
		var cookies = ATVI.utils.getCookies(true);
		if(cookies.comScore) data.comScore = cookies.comScore; 					
		
		data.ns_site = ATVI.utils.isProdSite() ? (this.ns_site || "dev") : "dev";
		
		for(var i in data) {
			loc += "&" + i + "=" + encodeURIComponent(data[i]);
		}
		
		if (loc.length > 2048) {
			var s = loc.substr(0, 2040).lastIndexOf("&");
			loc = (loc.substring(0, s) + "&ns_cut=" + esc(loc.substring(s + 1))).substr(0, 2048);
		}
		
		//alert(loc.split("&").join("\n&"));
		if($(".scorecard-container").length > 0)
			$(".scorecard-container").append('<img src="' + loc + '" height="1" width="1" alt="*" />') 
		else 
			$(document.body).append('<p class="scorecard-container"><img src="' + loc + '" height="1" width="1" alt="*" /></p>');
	},*/
	
	getVisitorId: function() {
		var cookies = ATVI.utils.getCookies(true);
		
		var ssoCookie = cookies.ACT_SSO_COOKIE || cookies.s_ACT_SSO_COOKIE; 
		
		if(ssoCookie) {
			var dec = ATVI.utils.decodeBase64(ssoCookie);
			var index = dec.indexOf(":");
			if(index >= 0) dec = dec.substring(0, index);
			return dec;
		}
		
		return this.getAnonVisitorId();
	},
	
	getAnonVisitorId: function() {
		
		var cookies = ATVI.utils.getCookies(true);
		
		if(cookies.ATVI_VISITOR_ID) return cookies.ATVI_VISITOR_ID;
		
		var date = new Date();
		var anonId = "anon-" + date.getTime() + "-" + Math.random();
		
		date.setTime(date.getTime() + 5 * 356 * 24 * 60 * 60000);
		//ATVI.utils.setCookie("ATVI_VISITOR_ID", anonId, date);
		
		return anonId;
	}
};

$(function() {
	if(window.ssobar && ssobar.onReady) {
		ssobar.onReady(function() {
			ATVI.analytics.init();
		});
	} else {
		ATVI.analytics.init();
	}
});

})(jQuery);