
## Hardware
### Power usage

Around 5.5-6.5W idle with stock 4GM RAM and 256GB Fanxiang mSATA (25€ eBay).

- Applied all 'Tunables' in `powertop`, but didn't change much.
- TODO `powertop --calibrate`


## Software
### Containers

Services are defined in `containers/**/docker-compose.yml` files.
Use `./run.sh` to start all or apply updates on changes.

### Network

Only reachable via intranet.
FritzBox resolves hostname `futro-s920`, but does not allow for subdomains on it.
Instead, added private IP for `*.edi.voglerr.de` on Cloudflare.
Adding `edi.voglerr.de` to the exceptions for FritzBox DNS rebind protection (Heimnetz > Netzwerk > Netzwerkeinstellungen > DNS-Rebind-Schutz) was enough to also allow subdomains (seems to be an undocumented bug since wildcards are not supported - [reddit](https://www.reddit.com/r/fritzbox/comments/18wozuu/7590_disable_dns_rebind_protection/)).
