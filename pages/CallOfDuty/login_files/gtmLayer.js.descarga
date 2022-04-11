var gtmLayer = gl = {};

var dataLayer = dataLayer || [];

var genGL = genGL || {};

genGL.init = function() {
	genGL.buildLayer();
	
};

genGL.getCookie = function (cookieName) {
	var i = 0,
		cookies = document.cookie.split(";"),
		length = cookies.length,
		trimRegex = /^\s+|\s+$/g,
		cookiePair;

	for (; i < length; i++) {
		cookiePair = cookies[i].split('=');
	
		if (cookiePair[0].replace(trimRegex, '') === cookieName) return unescape(cookiePair[1]);
	}
};

genGL.buildLayer = function() {
	gl.pushObj = {};
	
	genGL.buildLayerInfo();
	
	gl.pushObj.event = "pageview";
	dataLayer.push(gl.pushObj);
}

genGL.buildLayerInfo = function() {
	var communityId = genGL.getCookie("comid") || "unknown";
	var sitename = communityId;
	
	gl.pushObj.site = genGL.expandComId(communityId);
	gl.pushObj.siteSection = "sso-" + sitename.toLowerCase() + ":" + (communityId);
	gl.pushObj.siteSubsection = genGL.generatePage(communityId).toLowerCase();
	
	var page = genGL.generatePage(communityId)
	
	gl.pushObj.pageType = genGL.generatePageType(page);
	gl.pushObj.pageName = genGL.buildPageName(communityId);
	
	var name = genGL.buildCategory();
	gl.pushObj.name = gl.pushObj.pageName;
	var description = document.head.querySelector("[name~=description][content]").content;
	gl.pushObj.pageURL = window.location.origin + window.location.pathname;
	
	var locale = gl.pushObj.locale = genGL.getCookie("ACT_SSO_LOCALE") || "en_US";
	gl.pushObj.country = locale.split("_")[1].toLowerCase() || "";
	gl.pushObj.language = locale.split("_")[0].toLowerCase();
	
	gl.pushObj.charSet = "UTF-8";
	//var skill = "";
}

genGL.expandComId = function(comId) {
	switch (comId) {
		case "cod-mobile":
		case "cdl":
		case "cod":
			return "callofduty";
			break;
		case "hero":
			return "guitarhero";
			break;
		case "th":
			return "tony-hawk";
			break;
		default:
			return comId;
	}
};

genGL.buildPageName = function(communityId) {
	var page = genGL.buildCategory();
	var basePageName = genGL.expandComId(communityId);
	if(communityId == "th")
		basePageName = communityId;
	
	var primaryCategory = page.primaryCategory;
	if(communityId == "cod" || communityId == "cdl" || communityId == "cod-mobile")
		primaryCategory = "sso-callofduty";
	
	var additionalPageNameParam = "";
	if(communityId == "cod" || communityId == "cdl" || communityId == "cod-mobile")
		additionalPageNameParam = ":" + communityId;
	
	var subCategory = (genGL.generatePageType(genGL.generatePage(communityId)) == "home") ? "home" : page.subCategory1;
	
	return basePageName + ":" + primaryCategory + additionalPageNameParam + ":" + subCategory;
};

genGL.buildCategory = function() {
	var sitename = (genGL.getCookie("comid") == "cod") ? "callofduty" : (genGL.getCookie("comid") || "unknown");
	var page = genGL.generatePage(genGL.getCookie("comid") || "unknown")
	return {
		primaryCategory: "sso-" + sitename.toLowerCase(), // sitename
		subCategory1: page.toLowerCase(), // pagename
		pageType: genGL.generatePageType(page).toLowerCase()
	}
};

genGL.generatePage = function(sitename) {
	var page = window.location.pathname.split("/").pop();
	if(page == sitename || page == "")
		return "home";
	return page;
};

genGL.generatePageType = function(page) {
	if(page.toLowerCase().match("home"))
		return "home";
	else
		return "sub category";
};

genGL.getForm = function() {
	if(gl.pushObj.page.pageCategory.pageType == "login" || gl.pushObj.page.pageCategory.subCategory1 == "registrationdetails") {
		return {
			formName: $("form").attr("name") + ":account management"
		}
	} else {
		return "";
	}
};

genGL.init();