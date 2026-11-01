# Sample test cases

| # | Input URL | Expected result |
|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs; this does not prove the URL is safe. |
| 2 | `http://192.0.2.10/account` | IP-address hostname and HTTP warnings. |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol and HTTP warnings. |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Hostname-segment warning. |
| 5 | `https://xn--example.invalid/` | Punycode-marker warning. |

The automated test file also checks that blank input is rejected with a clear error.
