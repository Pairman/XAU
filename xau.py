from requests import get

def xau_get():
	url = "https://api.jijinhao.com/sQuoteCenter/realTime.htm"
	params = {"code": "JO_92233", "isCalc": True}
	headers = {
		"User-Agent":
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
		"KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
		"Referer": "https://www.cngold.org"
	}
	ret = {
		"name": "XAU", "prev_close": 0, "open": 0, "last_trade": 0,
		"high": 0, "low": 0, "change": 0, "percent_change": 0,
		"time": "", "err": ""
	}
	try:
		res = get(url, params = params, headers = headers)
		data = res.text[14 : -4].split(",")
		ret.update({
			"prev_close": float(data[2]),
			"open": float(data[38]), "last_trade": float(data[3]),
			"high": float(data[4]), "low": float(data[5]),
			"change": float(data[34]),
			"percent_change": float(data[35]),
			"bid": float(data[36]),
			"sell": float(data[37]),
			"time": f"{data[40]} {data[41]}"
		})
	except Exception as e:
		ret["err"] = f"{type(e).__name__}: {e}"
	finally:
		return ret
