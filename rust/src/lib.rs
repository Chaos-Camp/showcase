//! Links, before they are shortened.

/// Whether `url` is a web link this service will shorten.
pub fn is_web(url: &str) -> bool {
    url.starts_with("https://") || url.starts_with("http://")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn only_web_links() {
        assert!(is_web("https://example.com"));
        assert!(!is_web("ftp://example.com"));
    }
}
