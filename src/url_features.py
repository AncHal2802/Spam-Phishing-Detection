import re
from urllib.parse import urlparse
import tldextract

SUSPICIOUS_WORDS = ["login","verify","secure","account","update","bank","confirm","signin","paypal","free","bonus"]

def extract_url_features(url: str) -> dict:
    url = url.strip()
    parsed = urlparse(url if "://" in url else "http://" + url)
    host = parsed.netloc.split(":")[0]
    ext = tldextract.extract(url)

    return {
        "url_length":      len(url),
        "host_length":     len(host),
        "path_length":     len(parsed.path),
        "has_ip":          int(bool(re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", host))),
        "has_at":          int("@" in url),
        "num_dots":        url.count("."),
        "num_hyphens":     url.count("-"),
        "num_subdomains":  len([s for s in ext.subdomain.split(".") if s]),
        "num_digits":      sum(c.isdigit() for c in url),
        "num_params":      parsed.query.count("&") + (1 if parsed.query else 0),
        "https_scheme":    int(parsed.scheme == "https"),
        "https_in_host":   int("https" in host.lower()),
        "double_slash":    int(url.rfind("//") > 7),
        "suspicious_words":sum(w in url.lower() for w in SUSPICIOUS_WORDS),
        "is_shortener":    int(host.lower() in {"bit.ly","tinyurl.com","goo.gl","t.co","ow.ly","is.gd"}),
    }