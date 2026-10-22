//! Links, before they are shortened.

use regex::Regex;

/// Whether `url` is a web link this service will shorten.
pub fn is_web(url: &str) -> bool {
    url.starts_with("https://") || url.starts_with("http://")
}

/// Query parameters that only say where a click came from; two links that differ only in these
/// are the same link.
const TRACKING: &[&str] = &["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "gclid"];

/// The one form of a web link that is stored: the scheme and host lowercased, the default port, a
/// trailing slash and any fragment dropped, and tracking parameters removed. `None` for anything
/// that is not a web link.
pub fn normalize(url: &str) -> Option<String> {
    let parts = Regex::new(r"^(?i)(https?)://([^/?#:]+)(:\d+)?([^?#]*)(\?[^#]*)?").unwrap();
    let c = parts.captures(url.trim())?;
    let scheme = c[1].to_ascii_lowercase();
    let host = c[2].to_ascii_lowercase();
    let port = match (scheme.as_str(), c.get(3).map(|m| m.as_str())) {
        ("https", Some(":443")) | ("http", Some(":80")) | (_, None) => String::new(),
        (_, Some(p)) => p.to_owned(),
    };
    let path = c.get(4).map_or("", |m| m.as_str()).trim_end_matches('/');
    let kept: Vec<&str> = c
        .get(5)
        .map_or("", |m| &m.as_str()[1..])
        .split('&')
        .filter(|kv| !kv.is_empty() && !TRACKING.contains(&kv.split('=').next().unwrap_or("")))
        .collect();
    let query = if kept.is_empty() { String::new() } else { format!("?{}", kept.join("&")) };
    Some(format!("{scheme}://{host}{port}{path}{query}"))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn only_web_links() {
        assert!(is_web("https://example.com"));
        assert!(!is_web("ftp://example.com"));
    }

    #[test]
    fn one_link_one_form() {
        assert_eq!(normalize("HTTPS://Example.COM:443/docs/?utm_source=x&page=2#top").as_deref(), Some("https://example.com/docs?page=2"));
        assert_eq!(normalize("http://example.com:8080/").as_deref(), Some("http://example.com:8080"));
        assert_eq!(normalize("ftp://example.com"), None);
    }
}
