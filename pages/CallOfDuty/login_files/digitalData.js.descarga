var digitalData = dd = {};

var genDD = genDD || {};

genDD.init = function() {
	genDD.buildPage();
};

genDD.buildPage = function() {
	dd.page = {};

	genDD.buildPageInfo();
}

genDD.buildPageInfo = function() {
	var locale = SSO.utility.getCookie("ACT_SSO_LOCALE") || "en_US";
	var communityId = genDD.expandComId(SSO.utility.getCookie("comid") || "unknown");

	dd.page.pageCategory = genDD.buildCategory();
	dd.page.form = genDD.getForm();

	dd.page.pageInfo = {
		charSet: "UTF-8",
		country: locale.split("_")[1].toLowerCase() || "",
		language: locale.split("_")[0].toLowerCase(),
		pageName: genDD.buildPageName(communityId).toLowerCase(),
		site: communityId,
	}
};

genDD.expandComId = function(comId) {
	switch (comId) {
		case "cod":
			return "callofduty";
			break;
		case "hero":
			return "guitarhero";
			break;
		default:
			return comId;
	}
};

genDD.buildPageName = function(communityId) {
	return communityId + ":" + dd.page.pageCategory.primaryCategory + ":" + dd.page.pageCategory.subCategory1;
};

genDD.buildCategory = function() {
	var sitename = (config.siteId == "cod") ? "callofduty" : config.siteId;
	var page = genDD.generatePage(config.siteId)
	return {
		primaryCategory: "sso-" + sitename.toLowerCase(), // sitename
		subCategory1: page.toLowerCase(), // pagename
		pageType: genDD.generatePageType(page).toLowerCase()
	}
};

genDD.generatePage = function(sitename) {
	var page = window.location.pathname.split("/").pop();
	if(page == sitename || page == "")
		return "login";
	return page;
};

genDD.generatePageType = function(page) {
	switch(page) {
		case "login":
			return "login";
			break;
		case "register":
		case "registerThanks":
		case "registrationComplete":
		case "registrationDetails":
		case "validateEmail":
			return "registration";
			break;
		case "forgotPassword":
		case "childForgotUsername":
		case "childForgotPassword":
		case "childOptOut":
		case "removeAccount":
		case "resetPassword":
		case "maliciousResetPassword":
		case "missingProfileInformation":
		case "emailHelp":
		case "jiveLogout":
		case "optOut":
			return "accountmanagement"
			break;
		case "profile":
		case "prefs":
		case "profileLinked":
			return "profile"
			break;
		case "redeemCode":
		case "showBetaCodes":
			return "redemption";
			break;
		default:
			return "unknown";
			break;

	}
};

genDD.getForm = function() {
	if(dd.page.pageCategory.pageType == "login" || dd.page.pageCategory.subCategory1 == "registrationdetails") {
		return {
			formName: $("form").attr("name") + ":account management"
		}
	} else {
		return "";
	}
};

ssobar.onReady(genDD.init);