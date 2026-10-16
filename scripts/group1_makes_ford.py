"""
Ford Australia comprehensive historical data and complete model catalog.
"""
from typing import Any, Dict

FORD_DATA: Dict[str, Any] = {
    "make_slug": "ford",
    "name": "Ford Australia",
    "country_of_origin": "Australia",
    "years_active_au": {"start": 1925, "end": "Present"},
    "currently_sold_au": True,
    "local_manufacturer": True,
    "overview": "Ford Motor Company of Australia was established in Geelong, Victoria in March 1925 by Canadian-born Hubert French. Beginning with local assembly of the Model T in a disused wool store, Ford went on to become one of Australia's premier automotive manufacturers and innovators. In 1934, Ford Australia young designer Lewis Bandt invented the world's first coupe utility ('ute') in Geelong, creating an automotive category that defined rural and commercial Australia. In September 1960, Ford launched the Falcon, igniting a fierce 56-year rivalry with Holden. Operating major vehicle assembly and stamping complexes at Broadmeadows and engine and casting plants at Geelong, Ford designed, engineered, and manufactured iconic vehicles including the Falcon (XK through FG X), Fairlane, LTD, Territory SUV, and Capri convertible. Although local vehicle manufacturing ceased on 7 October 2016, Ford Australia transformed into Ford's Global Center of Excellence for Ranger and Everest, employing over 2,000 Australian engineers and designers at Campbellfield and the You Yangs Proving Ground.",
    "australian_history": "Ford's Australian journey began on 31 March 1925 when Ford Motor Company of Canada established its Australian subsidiary in Geelong, Victoria. Construction of a state-of-the-art manufacturing plant began immediately alongside plants in Brisbane, Sydney, Adelaide, and Perth. In 1934, responding to a farmer's wife's letter requesting 'a vehicle to go to church in on a Sunday and carry the pigs to market on Monday', 24-year-old Geelong designer Lewis Bandt penned the 1934 Ford Coupe Utility, grafting a cargo tray behind a 2-door coupe cabin—thus creating the 'Aussie Ute'.\n\nIn 1959, Ford established its new headquarters and main assembly plant at Broadmeadows, Melbourne. Rejecting the British Zephyr, managing director Charles Smith championed the American compact Falcon for local production. Launched in September 1960 as the XK Falcon, it initially suffered from fragile front ball joints on unsealed outback roads. Ford responded with the 1965 XP Falcon Durability Run, running five stock Falcons continuously for 70,000 miles at an average 70 mph at You Yangs to demonstrate rugged Australian durability—winning the 1965 Wheels Car of the Year.\n\nIn 1967, Ford ignited the Australian muscle car era with the XR Falcon GT (Windsor 289ci V8), followed by the legendary XY Falcon GT-HO Phase III in 1971. Powered by a 351ci Cleveland V8 and producing around 380 bhp, the Phase III was the fastest four-door production car on earth and Allan Moffat took it to back-to-back Bathurst victories. In 1972, Ford debuted the XA Falcon—the first Falcon entirely designed and developed in Australia, featuring the famous 'Coke bottle' hardtop coupe.\n\nFord dominated the 1980s with the XD, XE, and XF Falcon series, introducing Watts-linkage coil rear suspension, alloy cylinder heads, and electronic fuel injection, making the XF the best-selling car in Australia. The 2002 BA Falcon brought the revolutionary 4.0L DOHC 24-valve 'Barra' inline-six and Control Blade independent rear suspension, while the 2004 SX Territory became the first and only Australian-designed and built SUV, winning the 2004 Wheels COTY. Facing declining large-car sales, rising manufacturing costs, and the high Australian dollar, Ford concluded 91 years of vehicle production on 7 October 2016 when the last blue FG X Falcon XR6 sedan rolled off the Broadmeadows line. Today, Ford Australia thrives as an engineering and development powerhouse, leading global development of the best-selling Ford Ranger and Everest.",
    "models_catalog": [
        {
            "model_slug": "model-t",
            "name": "Ford Model T",
            "vehicle_type": "Tourer / Roadster / Commercial",
            "segment": "Vintage",
            "years_sold_au": {"start": 1925, "end": 1927},
            "locally_built": True,
            "overview": "The car that put Australia on wheels. Locally assembled in Geelong from Canadian knock-down kits starting in 1925, featuring rugged high ground clearance for outback tracks.",
            "generations": [
                {
                    "series_code": "Model-T",
                    "generation_name": "Australian Model T",
                    "years": {"start": 1925, "end": 1927},
                    "body_styles": ["Tourer", "Roadster", "Coupe", "Buckboard Ute"],
                    "summary": "2.9L (177ci) 4-cylinder engine (20 bhp), 2-speed planetary transmission, transverse leaf springs."
                }
            ]
        },
        {
            "model_slug": "model-a",
            "name": "Ford Model A",
            "vehicle_type": "Sedan / Coupe / Roadster / Phaeton / Ute",
            "segment": "Vintage",
            "years_sold_au": {"start": 1928, "end": 1931},
            "locally_built": True,
            "overview": "Successor to the Model T, offering modern controls, safety glass, standard four-wheel mechanical brakes, and handsome styling.",
            "generations": [
                {
                    "series_code": "Model-A",
                    "generation_name": "Australian Model A",
                    "years": {"start": 1928, "end": 1931},
                    "body_styles": ["Tudor Sedan", "Fordor Sedan", "Coupe", "Roadster", "Utility"],
                    "summary": "3.3L (201ci) L-head inline-4 (40 bhp), 3-speed sliding gear transmission, hydraulic shock absorbers."
                }
            ]
        },
        {
            "model_slug": "v8",
            "name": "Ford V8 (Model 18 / Custom / De Luxe)",
            "vehicle_type": "Sedan / Coupe / Coupe Utility",
            "segment": "Large",
            "years_sold_au": {"start": 1932, "end": 1954},
            "locally_built": True,
            "overview": "Pioneered mass-market V8 motoring in Australia with the Flathead V8, and birthed the world's first coupe utility in Geelong in 1934.",
            "generations": [
                {
                    "series_code": "Model-18-Custom",
                    "generation_name": "Ford Flathead V8 Series",
                    "years": {"start": 1932, "end": 1954},
                    "body_styles": ["Coupe Utility", "Sedan", "Coupe"],
                    "summary": "Legendary Flathead V8 (221ci, 239ci), birthplace of the Australian Ute in 1934 designed by Lewis Bandt."
                }
            ]
        },
        {
            "model_slug": "prefect",
            "name": "Ford Prefect",
            "vehicle_type": "Sedan / Utility",
            "segment": "Small",
            "years_sold_au": {"start": 1939, "end": 1962},
            "locally_built": True,
            "overview": "British Ford small family car assembled in Australia across E93A, E493A, and 100E generations, including local coupe utility variants.",
            "generations": [
                {
                    "series_code": "E93A-100E",
                    "generation_name": "Prefect Series",
                    "years": {"start": 1939, "end": 1962},
                    "body_styles": ["4-door sedan", "2-door coupe utility"],
                    "summary": "1,172cc side-valve and overhead-valve 4-cylinder engines; robust economy motoring."
                }
            ]
        },
        {
            "model_slug": "anglia",
            "name": "Ford Anglia",
            "vehicle_type": "Sedan / Van / Tourer",
            "segment": "Small",
            "years_sold_au": {"start": 1940, "end": 1967},
            "locally_built": True,
            "overview": "Popular British-designed small car assembled in Australia, concluding with the iconic reverse-rake rear window 105E.",
            "generations": [
                {
                    "series_code": "E04A-105E",
                    "generation_name": "Anglia Series",
                    "years": {"start": 1940, "end": 1967},
                    "body_styles": ["2-door sedan", "Tourer", "Van"],
                    "summary": "From side-valve 933cc to the rev-happy 997cc Kent OHV engine in the backward-slanted rear window 105E."
                }
            ]
        },
        {
            "model_slug": "consul",
            "name": "Ford Consul",
            "vehicle_type": "Sedan / Wagon / Utility",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1951, "end": 1962},
            "locally_built": True,
            "overview": "Modern unibody sedan with MacPherson strut front suspension, assembled in Australia with unique local ute variants.",
            "generations": [
                {
                    "series_code": "Mk-I-II",
                    "generation_name": "Consul Mark I & II",
                    "years": {"start": 1951, "end": 1962},
                    "body_styles": ["4-door sedan", "Coupe utility", "Wagon"],
                    "summary": "1.5L and 1.7L OHV 4-cylinder engines, unibody construction, Australian-developed utility body."
                }
            ]
        },
        {
            "model_slug": "zephyr",
            "name": "Ford Zephyr",
            "vehicle_type": "Sedan / Wagon / Utility",
            "segment": "Large",
            "years_sold_au": {"start": 1951, "end": 1966},
            "locally_built": True,
            "overview": "Six-cylinder flagship of British Ford, manufactured with high local content in Geelong and Broadmeadows before being superseded by the Falcon.",
            "generations": [
                {
                    "series_code": "Mk-I-III",
                    "generation_name": "Zephyr Mark I, II, III",
                    "years": {"start": 1951, "end": 1966},
                    "body_styles": ["4-door sedan", "Coupe utility", "Station wagon"],
                    "summary": "2.3L and 2.6L OHV inline-six engines, front disc brakes on Mk II/III, iconic Zodiac luxury variant."
                }
            ]
        },
        {
            "model_slug": "zodiac",
            "name": "Ford Zodiac",
            "vehicle_type": "Sedan",
            "segment": "Luxury",
            "years_sold_au": {"start": 1953, "end": 1966},
            "locally_built": True,
            "overview": "Upmarket luxury variant of the Zephyr featuring two-tone paint, leather seating, whitewall tyres, and twin carburettors.",
            "generations": [
                {
                    "series_code": "Mk-I-III",
                    "generation_name": "Zodiac Mark I, II, III",
                    "years": {"start": 1953, "end": 1966},
                    "body_styles": ["4-door luxury sedan"],
                    "summary": "2.6L straight-six, overdrive gearbox or Borg-Warner automatic, luxury appointments."
                }
            ]
        },
        {
            "model_slug": "cortina",
            "name": "Ford Cortina",
            "vehicle_type": "Sedan / Wagon",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1962, "end": 1982},
            "locally_built": True,
            "overview": "Major seller spanning British Mk I & II imports/assembly to uniquely Australian six-cylinder TC, TD, TE, and TF series packing Falcon 200ci and 250ci engines.",
            "generations": [
                {
                    "series_code": "Mk-I-II",
                    "generation_name": "Cortina Mk I & Mk II",
                    "years": {"start": 1962, "end": 1971},
                    "body_styles": ["2-door sedan", "4-door sedan", "Station wagon"],
                    "summary": "1.2L, 1.5L, and 1.6L Kent engines, GT performance models with dual Weber carburettors."
                },
                {
                    "series_code": "TC-TF",
                    "generation_name": "Cortina Six (TC, TD, TE, TF)",
                    "years": {"start": 1971, "end": 1982},
                    "body_styles": ["4-door sedan", "5-door wagon"],
                    "summary": "Re-engineered with longer nose to package Falcon 3.3L and 4.1L inline-six engines; the famous 'Cortina 6'."
                }
            ]
        },
        {
            "model_slug": "escort",
            "name": "Ford Escort",
            "vehicle_type": "Sedan / Panel Van",
            "segment": "Small",
            "years_sold_au": {"start": 1970, "end": 1981},
            "locally_built": True,
            "overview": "Agile rear-wheel-drive small car built at Homebush, NSW. Famous for Bathurst class wins and rally dominance with Twin Cam and RS2000 models.",
            "generations": [
                {
                    "series_code": "Mk-I-II",
                    "generation_name": "Escort Mk I & Mk II",
                    "years": {"start": 1970, "end": 1981},
                    "body_styles": ["2-door sedan", "4-door sedan", "2-door panel van"],
                    "summary": "1.1L, 1.3L, 1.6L Kent engines, and the iconic 2.0L Pinto-powered RS2000 with polyurethane droop-snoot nose."
                }
            ]
        },
        {
            "model_slug": "capri",
            "name": "Ford Capri",
            "vehicle_type": "Coupe / Convertible",
            "segment": "Sports",
            "years_sold_au": {"start": 1969, "end": 1994},
            "locally_built": True,
            "overview": "First sold as the British fastback coupe (Mk I 1600 & 3000 GT), then revived as an Australian-designed and built 2+2 roadster (SA-SE) exported to the US as the Mercury Capri.",
            "generations": [
                {
                    "series_code": "Mk-I",
                    "generation_name": "Capri Mk I Coupe",
                    "years": {"start": 1969, "end": 1973},
                    "body_styles": ["2-door fastback coupe"],
                    "summary": "Assembled at Homebush; 1.6L Kent and 3.0L Essex V6 GT."
                },
                {
                    "series_code": "SA-SE",
                    "generation_name": "Australian Capri Roadster (SA, SB, SC, SE)",
                    "years": {"start": 1989, "end": 1994},
                    "body_styles": ["2-door convertible"],
                    "summary": "Mazda 323 platform, turbocharged B6T 1.6L twin-cam, pop-up headlights; over 66,000 built at Broadmeadows for worldwide export."
                }
            ]
        },
        {
            "model_slug": "falcon",
            "name": "Ford Falcon",
            "vehicle_type": "Sedan / Wagon / Coupe",
            "segment": "Large",
            "years_sold_au": {"start": 1960, "end": 2016},
            "locally_built": True,
            "overview": "The heartbeat of Ford Australia for 56 continuous years. Over 3.5 million manufactured at Broadmeadows across 7 generations from the XK to the FG X, boasting legendary XR6, XR8, and GT-HO models.",
            "generations": [
                {
                    "series_code": "XK-XP",
                    "generation_name": "First Generation (XK, XL, XM, XP)",
                    "years": {"start": 1960, "end": 1966},
                    "body_styles": ["Sedan", "Wagon", "Hardtop Coupe"],
                    "summary": "Pioneered Falcon in Australia; XP 70,000-mile Durability Run won 1965 Wheels COTY; 144, 170, and 200ci Pursuit sixes."
                },
                {
                    "series_code": "XR-XY",
                    "generation_name": "Second Generation (XR, XT, XW, XY)",
                    "years": {"start": 1966, "end": 1972},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "Mustang-bred styling; birth of XR Falcon GT (289 V8); XY GT-HO Phase III (351 Cleveland V8) fastest 4-door production car."
                },
                {
                    "series_code": "XA-XC",
                    "generation_name": "Third Generation (XA, XB, XC)",
                    "years": {"start": 1972, "end": 1979},
                    "body_styles": ["Sedan", "Wagon", "Hardtop Coupe"],
                    "summary": "First all-Australian designed Falcon; iconic 2-door Hardtop, Mad Max Interceptor (XB GT), and 1977 Bathurst 1-2 Moffat/Bond finish."
                },
                {
                    "series_code": "XD-XF",
                    "generation_name": "Fourth Generation (XD, XE, XF)",
                    "years": {"start": 1979, "end": 1988},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "European styling; alloy cylinder head, Watts-linkage rear suspension on XE, EFI; XF became Australia's top-selling car."
                },
                {
                    "series_code": "EA-EL",
                    "generation_name": "Fifth Generation (EA, EB, ED, EF, EL)",
                    "years": {"start": 1988, "end": 1998},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "Aero styling with 3.9L/4.0L OHC I6; return of 5.0L Windsor V8 in EB; birth of XR6 and XR8 with Tickford Vehicle Engineering."
                },
                {
                    "series_code": "AU",
                    "generation_name": "Sixth Generation - AU Series (AU I, II, III)",
                    "years": {"start": 1998, "end": 2002},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "New Edge design; Intech 4.0L I6 with VCT, double-wishbone IRS option, high-output XR8 V8s up to 220kW."
                },
                {
                    "series_code": "BA-BF",
                    "generation_name": "Sixth Generation - BA & BF Series",
                    "years": {"start": 2002, "end": 2008},
                    "body_styles": ["Sedan", "Wagon"],
                    "summary": "Barra 182/190 DOHC 24V I6, Barra 240T/245T Turbo, Boss 260/290 5.4L V8, Control Blade IRS, ZF 6-speed auto; Wheels COTY 2002."
                },
                {
                    "series_code": "FG-FGX",
                    "generation_name": "Seventh Generation - FG & FG X Series",
                    "years": {"start": 2008, "end": 2016},
                    "body_styles": ["Sedan"],
                    "summary": "First Australian car with 5-star ANCAP safety; Barra 195, Barra 270T/310T Turbo, EcoBoost 2.0T, Supercharged Miami 5.0L V8, Sprint 6 and Sprint 8."
                }
            ]
        },
        {
            "model_slug": "falcon-ute",
            "name": "Ford Falcon Utility & Panel Van",
            "vehicle_type": "Coupe Utility / Panel Van / Cab Chassis",
            "segment": "Commercial",
            "years_sold_au": {"start": 1961, "end": 2016},
            "locally_built": True,
            "overview": "The definitive Australian workhorse and recreational vehicle, offering unmatched durability, leaf-spring load-carrying capability, and legendary XR6 Turbo and XR8 performance trims.",
            "generations": [
                {
                    "series_code": "XK-FGX-Ute",
                    "generation_name": "Falcon Ute & Van (XK through FG X)",
                    "years": {"start": 1961, "end": 2016},
                    "body_styles": ["Coupe Utility", "Cab Chassis", "Panel Van"],
                    "summary": "Spanned 55 years of Australian commercial dominance, from early Pursuits to AU/BA/FG cab-chassis and XR6 Turbo / XR8 performance utes."
                }
            ]
        },
        {
            "model_slug": "fairlane-ltd",
            "name": "Ford Fairlane & LTD",
            "vehicle_type": "Sedan",
            "segment": "Upper Luxury / Limousine",
            "years_sold_au": {"start": 1967, "end": 2007},
            "locally_built": True,
            "overview": "Australia's top-selling luxury limousine for decades, pioneering long-wheelbase elegance, standard V8 power, and presidential transport across ZA through BF generations.",
            "generations": [
                {
                    "series_code": "ZA-ZD",
                    "generation_name": "Fairlane ZA to ZD",
                    "years": {"start": 1967, "end": 1972},
                    "body_styles": ["4-door long-wheelbase sedan"],
                    "summary": "Stretched 116-inch wheelbase Falcon body; 289, 302, and 351 Windsor/Cleveland V8s."
                },
                {
                    "series_code": "ZF-ZH-P5-P6",
                    "generation_name": "Fairlane ZF-ZH & LTD P5-P6",
                    "years": {"start": 1972, "end": 1979},
                    "body_styles": ["4-door long-wheelbase sedan"],
                    "summary": "Introduction of the ultra-luxurious LTD (121-inch wheelbase) with hidden headlamps and 351 Cleveland V8."
                },
                {
                    "series_code": "ZJ-ZL-FC-FE",
                    "generation_name": "Fairlane ZJ-ZL & LTD FC-FE",
                    "years": {"start": 1979, "end": 1988},
                    "body_styles": ["4-door luxury sedan"],
                    "summary": "Crisp European aesthetic; alloy-head 4.1L EFI six, digital electronic instrumentation."
                },
                {
                    "series_code": "NA-NL-DA-DL",
                    "generation_name": "Fairlane NA-NL & LTD DA-DL",
                    "years": {"start": 1988, "end": 1999},
                    "body_styles": ["4-door luxury sedan"],
                    "summary": "Aero body, 3.9L/4.0L OHC I6, 5.0L Windsor V8, Fairlane By Tickford performance edition."
                },
                {
                    "series_code": "AU-BA-BF",
                    "generation_name": "Fairlane & LTD (AU, BA, BF)",
                    "years": {"start": 1999, "end": 2007},
                    "body_styles": ["4-door luxury sedan"],
                    "summary": "IRS rear suspension, Barra 182/190 I6, Barra 220 5.4L 3V V8, G220 sports model, and ZF 6-speed automatic."
                }
            ]
        },
        {
            "model_slug": "landau",
            "name": "Ford Landau",
            "vehicle_type": "Hardtop Coupe",
            "segment": "Personal Luxury Coupe",
            "years_sold_au": {"start": 1973, "end": 1976},
            "locally_built": True,
            "overview": "Exclusive two-door personal luxury coupe combining the Falcon Hardtop body with the opulent front clip of the P5 LTD, featuring pop-up headlight shutters and standard 351 Cleveland V8.",
            "generations": [
                {
                    "series_code": "JG70",
                    "generation_name": "Landau JG70 Series",
                    "years": {"start": 1973, "end": 1976},
                    "body_styles": ["2-door hardtop coupe"],
                    "summary": "Standard 351 Cleveland V8 (290 bhp), four-wheel disc brakes, vacuum-operated concealed headlights, vinyl roof; only 1,385 produced."
                }
            ]
        },
        {
            "model_slug": "territory",
            "name": "Ford Territory",
            "vehicle_type": "SUV",
            "segment": "Medium / Large SUV",
            "years_sold_au": {"start": 2004, "end": 2016},
            "locally_built": True,
            "overview": "The first and only SUV designed, engineered, and manufactured in Australia. Winner of the 2004 Wheels Car of the Year, offering 5- or 7-seat packaging, RWD and AWD, and Barra Turbo / Duratorq V6 diesel powertrains.",
            "generations": [
                {
                    "series_code": "SX",
                    "generation_name": "Territory SX Series",
                    "years": {"start": 2004, "end": 2005},
                    "body_styles": ["5-door SUV (5 or 7 seats)"],
                    "summary": "2004 Wheels COTY winner; Barra 182 4.0L I6, Virtual Pivot Control front suspension, Control Blade rear IRS, TX, TS, Ghia."
                },
                {
                    "series_code": "SY",
                    "generation_name": "Territory SY & SY II Series",
                    "years": {"start": 2005, "end": 2011},
                    "body_styles": ["5-door SUV"],
                    "summary": "Barra 190 I6, ZF 6-speed auto, and blistering 245kW Territory Turbo and Turbo Ghia variants."
                },
                {
                    "series_code": "SZ",
                    "generation_name": "Territory SZ & SZ II Series",
                    "years": {"start": 2011, "end": 2016},
                    "body_styles": ["5-door SUV"],
                    "summary": "Introduction of the 2.7L V6 Duratorq Turbo Diesel (TDCi), electric power steering, SYNC infotainment; final Australian-built SUV."
                }
            ]
        },
        {
            "model_slug": "laser",
            "name": "Ford Laser",
            "vehicle_type": "Hatchback / Sedan",
            "segment": "Small",
            "years_sold_au": {"start": 1981, "end": 2002},
            "locally_built": True,
            "overview": "Sensational small-car success engineered in partnership with Mazda and assembled at Homebush, NSW through KA to KH series. Renowned for sporting Sport, TX3, and Turbo 4WD variants.",
            "generations": [
                {
                    "series_code": "KA-KB",
                    "generation_name": "Laser KA & KB Series",
                    "years": {"start": 1981, "end": 1985},
                    "body_styles": ["3-door hatchback", "5-door hatchback"],
                    "summary": "Mazda 323 platform, E-series 1.3L and 1.5L engines, Sport model; instant sales sensation."
                },
                {
                    "series_code": "KC-KE",
                    "generation_name": "Laser KC & KE Series",
                    "years": {"start": 1985, "end": 1990},
                    "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan", "Station wagon"],
                    "summary": "B6 1.6L EFI and iconic TX3 Turbo and TX3 Turbo 4WD hot hatches."
                },
                {
                    "series_code": "KF-KH",
                    "generation_name": "Laser KF & KH Series",
                    "years": {"start": 1990, "end": 1994},
                    "body_styles": ["Hatchback", "Sedan"],
                    "summary": "1.6L and 1.8L DOHC BP engines; legendary TX3 4WD Turbo with 16-valve BPT engine."
                },
                {
                    "series_code": "KJ-KQ",
                    "generation_name": "Laser KJ, KL, KN, KQ Series",
                    "years": {"start": 1994, "end": 2002},
                    "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan"],
                    "summary": "Imported from Japan; Lynx hatchback, 1.8L and 2.0L FS-DE engines, succeeded by the Focus."
                }
            ]
        },
        {
            "model_slug": "meteor",
            "name": "Ford Meteor",
            "vehicle_type": "Sedan / Wagon",
            "segment": "Small",
            "years_sold_au": {"start": 1982, "end": 1987},
            "locally_built": True,
            "overview": "The sedan and wagon sibling to the Laser hatchback, assembled at Homebush, NSW with upscale frontal styling and plush trim.",
            "generations": [
                {
                    "series_code": "GA-GC",
                    "generation_name": "Meteor GA, GB, GC Series",
                    "years": {"start": 1982, "end": 1987},
                    "body_styles": ["4-door sedan", "5-door wagon"],
                    "summary": "1.5L and 1.6L engines; GL and Ghia trim levels; integrated into the Laser sedan line in 1987."
                }
            ]
        },
        {
            "model_slug": "telstar",
            "name": "Ford Telstar",
            "vehicle_type": "Hatchback / Sedan",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1983, "end": 1999},
            "locally_built": True,
            "overview": "Highly successful mid-size car built in Australia (AR-AT) and later imported from Japan (AV-AY), sharing engineering with the Mazda 626.",
            "generations": [
                {
                    "series_code": "AR-AT",
                    "generation_name": "Telstar AR, AS, AT (Locally Built)",
                    "years": {"start": 1983, "end": 1992},
                    "body_styles": ["4-door sedan", "5-door hatchback"],
                    "summary": "Wheels COTY 1983 winner; 2.0L and 2.2L 12V engines, TX5 sports hatchback, Turbo model."
                },
                {
                    "series_code": "AV-AY",
                    "generation_name": "Telstar AV, AX, AY (Imported)",
                    "years": {"start": 1992, "end": 1999},
                    "body_styles": ["Sedan", "Hatchback"],
                    "summary": "Sleek organic styling with 2.0L inline-4 and 2.5L 24V KL-DE V6."
                }
            ]
        },
        {
            "model_slug": "corsair",
            "name": "Ford Corsair",
            "vehicle_type": "Sedan / Hatchback",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1989, "end": 1992},
            "locally_built": True,
            "overview": "Badge-engineered Nissan Pintara built under the Button Car Plan at Nissan's Clayton, Victoria plant.",
            "generations": [
                {
                    "series_code": "UA",
                    "generation_name": "Corsair UA Series",
                    "years": {"start": 1989, "end": 1992},
                    "body_styles": ["4-door sedan", "5-door hatchback"],
                    "summary": "Nissan CA20E 2.0L and KA24E 2.4L SOHC engines; GL and Ghia specifications."
                }
            ]
        },
        {
            "model_slug": "festiva",
            "name": "Ford Festiva",
            "vehicle_type": "Hatchback / Sedan",
            "segment": "Light",
            "years_sold_au": {"start": 1991, "end": 2000},
            "locally_built": False,
            "overview": "Popular entry-level light car engineered by Mazda and built by Kia in South Korea, offering affordable and dependable city transport.",
            "generations": [
                {
                    "series_code": "WA-WF",
                    "generation_name": "Festiva WA, WB, WD, WF Series",
                    "years": {"start": 1991, "end": 2000},
                    "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan"],
                    "summary": "1.3L and 1.5L 4-cylinder engines; Trio, GLi, and sporty Festiva Trio S variants."
                }
            ]
        },
        {
            "model_slug": "fiesta",
            "name": "Ford Fiesta",
            "vehicle_type": "Hatchback",
            "segment": "Light / Hot Hatch",
            "years_sold_au": {"start": 2004, "end": 2022},
            "locally_built": False,
            "overview": "Dynamic European light hatchback renowned for benchmark chassis tuning, culminating in the award-winning Fiesta ST hot hatch.",
            "generations": [
                {
                    "series_code": "WP-WZ",
                    "generation_name": "Fiesta WP through WZ",
                    "years": {"start": 2004, "end": 2022},
                    "body_styles": ["3-door hatchback", "5-door hatchback"],
                    "summary": "1.6L Duratec, 1.0L EcoBoost 3-cylinder, and the sensational 1.6L/1.5L Turbo Fiesta ST."
                }
            ]
        },
        {
            "model_slug": "focus",
            "name": "Ford Focus",
            "vehicle_type": "Hatchback / Sedan / Wagon",
            "segment": "Small / Hot Hatch",
            "years_sold_au": {"start": 2002, "end": 2022},
            "locally_built": False,
            "overview": "European-engineered small car acclaimed for Control Blade independent rear suspension dynamics, spawning the legendary ST and AWD Focus RS.",
            "generations": [
                {
                    "series_code": "LR-SA",
                    "generation_name": "Focus LR through SA Series",
                    "years": {"start": 2002, "end": 2022},
                    "body_styles": ["Hatchback", "Sedan", "Wagon"],
                    "summary": "From LR to Mk4 SA; 2.0L Duratec, 1.5L EcoBoost, 2.5L 5-cylinder XR5 Turbo, and 257kW AWD Focus RS."
                }
            ]
        },
        {
            "model_slug": "mondeo",
            "name": "Ford Mondeo",
            "vehicle_type": "Sedan / Hatchback / Wagon",
            "segment": "Mid-size",
            "years_sold_au": {"start": 1995, "end": 2020},
            "locally_built": False,
            "overview": "Sophisticated European mid-size family car imported across four generations, featuring 2.5L V6, 2.0L EcoBoost, and efficient TDCi diesels.",
            "generations": [
                {
                    "series_code": "HA-MD",
                    "generation_name": "Mondeo First through Fourth Gen",
                    "years": {"start": 1995, "end": 2020},
                    "body_styles": ["Sedan", "Hatchback", "Wagon"],
                    "summary": "Zetec, Duratec 2.5L V6, 2.5L 5-cylinder Turbo (XR5), 2.0L EcoBoost (177kW), and Duratorq diesel."
                }
            ]
        },
        {
            "model_slug": "taurus",
            "name": "Ford Taurus",
            "vehicle_type": "Sedan",
            "segment": "Large",
            "years_sold_au": {"start": 1996, "end": 1998},
            "locally_built": False,
            "overview": "Radical oval-themed American sedan imported to complement the Falcon in Ghia luxury trim.",
            "generations": [
                {
                    "series_code": "DP",
                    "generation_name": "Taurus DP Ghia",
                    "years": {"start": 1996, "end": 1998},
                    "body_styles": ["4-door sedan"],
                    "summary": "3.0L Duratec 24V DOHC V6 (149kW), four-speed automatic, radical bio-design curves."
                }
            ]
        },
        {
            "model_slug": "cougar",
            "name": "Ford Cougar",
            "vehicle_type": "Coupe",
            "segment": "Sports Coupe",
            "years_sold_au": {"start": 1999, "end": 2004},
            "locally_built": False,
            "overview": "Striking New Edge styling coupe imported from Ford of Germany, based on the Mondeo platform.",
            "generations": [
                {
                    "series_code": "SW",
                    "generation_name": "Cougar SW Series",
                    "years": {"start": 1999, "end": 2004},
                    "body_styles": ["3-door liftback coupe"],
                    "summary": "2.5L Duratec 24V V6 (125kW), independent suspension, leather trim, 5-speed manual or 4-speed auto."
                }
            ]
        },
        {
            "model_slug": "probe",
            "name": "Ford Probe",
            "vehicle_type": "Coupe",
            "segment": "Sports Coupe",
            "years_sold_au": {"start": 1994, "end": 1998},
            "locally_built": False,
            "overview": "Aerodynamic liftback sports coupe built in the USA in partnership with Mazda, featuring pop-up headlamps and a quad-cam V6.",
            "generations": [
                {
                    "series_code": "ST-SU",
                    "generation_name": "Probe ST & SU Series",
                    "years": {"start": 1994, "end": 1998},
                    "body_styles": ["2-door liftback coupe"],
                    "summary": "2.5L KL-DE 24V DOHC V6 (121kW), 5-speed manual or 4-speed auto, 4-wheel disc brakes with ABS."
                }
            ]
        },
        {
            "model_slug": "ka",
            "name": "Ford Ka",
            "vehicle_type": "Hatchback",
            "segment": "City Car / Micro",
            "years_sold_au": {"start": 1999, "end": 2002},
            "locally_built": False,
            "overview": "Funky European city car showcasing Ford's dramatic New Edge design philosophy with unpainted scratch-resistant bumpers.",
            "generations": [
                {
                    "series_code": "TA",
                    "generation_name": "Ka TA Series",
                    "years": {"start": 1999, "end": 2002},
                    "body_styles": ["3-door hatchback"],
                    "summary": "1.3L Endura-E 4-cylinder engine, 5-speed manual, go-kart handling dynamics."
                }
            ]
        },
        {
            "model_slug": "ecosport",
            "name": "Ford EcoSport",
            "vehicle_type": "Compact SUV",
            "segment": "Small SUV",
            "years_sold_au": {"start": 2013, "end": 2020},
            "locally_built": False,
            "overview": "High-riding urban mini-SUV featuring external tailgate-mounted spare wheel and efficient EcoBoost powertrains.",
            "generations": [
                {
                    "series_code": "BK",
                    "generation_name": "EcoSport BK Series",
                    "years": {"start": 2013, "end": 2020},
                    "body_styles": ["5-door compact SUV"],
                    "summary": "1.0L 3-cylinder EcoBoost Turbo and 1.5L Ti-VCT petrol engines; Ambiente, Trend, Titanium."
                }
            ]
        },
        {
            "model_slug": "kuga",
            "name": "Ford Kuga",
            "vehicle_type": "Medium SUV",
            "segment": "Medium SUV",
            "years_sold_au": {"start": 2012, "end": 2016},
            "locally_built": False,
            "overview": "German-engineered medium crossover offering punchy turbo engines and intelligent all-wheel drive, later badged Escape.",
            "generations": [
                {
                    "series_code": "TF",
                    "generation_name": "Kuga TF Series",
                    "years": {"start": 2012, "end": 2016},
                    "body_styles": ["5-door SUV"],
                    "summary": "1.5L/1.6L/2.0L EcoBoost turbo petrol and 2.0L TDCi turbo-diesel; hands-free sensor tailgate."
                }
            ]
        },
        {
            "model_slug": "escape",
            "name": "Ford Escape",
            "vehicle_type": "Medium SUV",
            "segment": "Medium SUV",
            "years_sold_au": {"start": 2001, "end": 2023},
            "locally_built": False,
            "overview": "Long-running mid-size SUV spanning joint-venture Mazda Tribute platform iterations through modern European turbocharged models and plug-in hybrid (PHEV).",
            "generations": [
                {
                    "series_code": "BA-ZD",
                    "generation_name": "Escape First Generation (BA-ZD)",
                    "years": {"start": 2001, "end": 2012},
                    "body_styles": ["5-door SUV"],
                    "summary": "Mazda co-developed platform; 2.0L/2.3L 4-cylinder and 3.0L Duratec V6 with Control Trac II 4WD."
                },
                {
                    "series_code": "ZG-ZH",
                    "generation_name": "Escape Second & Third Gen (ZG, ZH)",
                    "years": {"start": 2016, "end": 2023},
                    "body_styles": ["5-door SUV"],
                    "summary": "178kW 2.0L EcoBoost, 2.5L Plug-in Hybrid (PHEV), ST-Line sport styling, and SYNC 3."
                }
            ]
        },
        {
            "model_slug": "endura",
            "name": "Ford Endura",
            "vehicle_type": "Large SUV",
            "segment": "Large 5-Seat SUV",
            "years_sold_au": {"start": 2018, "end": 2020},
            "locally_built": False,
            "overview": "Canadian-built premium 5-seat crossover (Ford Edge in North America) powered exclusively by a bi-turbo diesel engine.",
            "generations": [
                {
                    "series_code": "CA",
                    "generation_name": "Endura CA Series",
                    "years": {"start": 2018, "end": 2020},
                    "body_styles": ["5-door SUV"],
                    "summary": "2.0L Bi-Turbo EcoBlue Diesel (140kW/400Nm), 8-speed automatic, Trend, ST-Line, and Titanium."
                }
            ]
        },
        {
            "model_slug": "everest",
            "name": "Ford Everest",
            "vehicle_type": "4WD SUV",
            "segment": "Large 4WD 7-Seat SUV",
            "years_sold_au": {"start": 2015, "end": "Present"},
            "locally_built": False,
            "overview": "Tough 7-seat body-on-frame 4WD engineered in Victoria by Ford Australia on the Ranger T6 architecture with coil-sprung Watts-link rear suspension.",
            "generations": [
                {
                    "series_code": "UA",
                    "generation_name": "Everest First Generation (UA)",
                    "years": {"start": 2015, "end": 2022},
                    "body_styles": ["5-door 7-seat 4WD"],
                    "summary": "3.2L 5-cylinder TDCi and 2.0L Bi-Turbo diesel; Terrain Management System, 3.1-tonne towing."
                },
                {
                    "series_code": "UB",
                    "generation_name": "Everest Next-Gen (UB)",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["5-door 7-seat 4WD"],
                    "summary": "3.0L V6 Turbo Diesel (184kW/600Nm) and 2.0L Bi-Turbo, full-time 4WD, 3.5t towing, 12-inch portrait touchscreen."
                }
            ]
        },
        {
            "model_slug": "puma",
            "name": "Ford Puma",
            "vehicle_type": "Compact Crossover",
            "segment": "Small SUV",
            "years_sold_au": {"start": 2020, "end": "Present"},
            "locally_built": False,
            "overview": "Romanian-built stylish European small crossover with mild-hybrid 1.0L EcoBoost powertrain and innovative MegaBox boot storage.",
            "generations": [
                {
                    "series_code": "JK",
                    "generation_name": "Puma JK Series",
                    "years": {"start": 2020, "end": "Present"},
                    "body_styles": ["5-door crossover"],
                    "summary": "1.0L 3-cylinder EcoBoost mHEV (92kW), 7-speed dual-clutch transmission, ST-Line, ST-Line V, Puma ST."
                }
            ]
        },
        {
            "model_slug": "mustang",
            "name": "Ford Mustang",
            "vehicle_type": "Coupe / Convertible",
            "segment": "Sports Car",
            "years_sold_au": {"start": 1965, "end": "Present"},
            "locally_built": False,
            "overview": "The world's most iconic pony car. Imported in small RHD batches in 1965-66, factory RHD converted by Tickford in 2001-02, and officially sold in factory RHD from 2015, becoming Australia's top-selling sports car.",
            "generations": [
                {
                    "series_code": "1965-AU",
                    "generation_name": "First Gen Australian Converted",
                    "years": {"start": 1965, "end": 1966},
                    "body_styles": ["Hardtop coupe"],
                    "summary": "Officially converted by Ford Australia at Homebush; 289 V8; highly prized rarity."
                },
                {
                    "series_code": "SN95-Tickford",
                    "generation_name": "FTE Cobra Mustang",
                    "years": {"start": 2001, "end": 2002},
                    "body_styles": ["Coupe", "Convertible"],
                    "summary": "Hand-converted to RHD by Tickford Vehicle Engineering; 4.6L DOHC 32V SVT V8 (240kW)."
                },
                {
                    "series_code": "S550",
                    "generation_name": "Sixth Generation (S550)",
                    "years": {"start": 2015, "end": 2023},
                    "body_styles": ["Fastback coupe", "Convertible"],
                    "summary": "First global factory RHD Mustang. 2.3L EcoBoost and 5.0L Coyote V8 (339kW), Mach 1, Bullitt, R-Spec (supercharged 522kW)."
                },
                {
                    "series_code": "S650",
                    "generation_name": "Seventh Generation (S650)",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["Fastback coupe", "Convertible"],
                    "summary": "Gen-4 5.0L Coyote V8, dual air intakes, dual throttle bodies, Dark Horse 373kW flagship."
                }
            ]
        },
        {
            "model_slug": "f-series",
            "name": "Ford F-Series (F-100 / F-150 / F-250)",
            "vehicle_type": "Full-size Pick-up",
            "segment": "Large Commercial Pick-up",
            "years_sold_au": {"start": 1948, "end": "Present"},
            "locally_built": True,
            "overview": "The undisputed heavy lifter of regional Australia. Assembled locally in Brisbane and Broadmeadows with local six and V8 engines through 1992, and revived in factory-backed RHD remanufacturing programs.",
            "generations": [
                {
                    "series_code": "F-Series-AU",
                    "generation_name": "Australian Built F-100/F-250/F-350",
                    "years": {"start": 1948, "end": 1992},
                    "body_styles": ["Single Cab", "Super Cab", "Cab Chassis"],
                    "summary": "Locally assembled with Falcon 250 Crossflow sixes and 302/351 Cleveland V8s; tough twin I-beam suspension."
                },
                {
                    "series_code": "F-150-Modern",
                    "generation_name": "Modern F-150 Remanufactured",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["SuperCrew Cab"],
                    "summary": "Officially remanufactured to RHD in Melbourne by RMA Automotive; 3.5L EcoBoost V6 (298kW/678Nm), 4.5t towing."
                }
            ]
        },
        {
            "model_slug": "courier",
            "name": "Ford Courier",
            "vehicle_type": "Ute / Cab Chassis",
            "segment": "Commercial Pick-up",
            "years_sold_au": {"start": 1978, "end": 2006},
            "locally_built": False,
            "overview": "Durable Japanese and Thai-built compact and mid-size commercial utility developed in partnership with Mazda (B-Series).",
            "generations": [
                {
                    "series_code": "PC-PH",
                    "generation_name": "Courier PC through PH Series",
                    "years": {"start": 1978, "end": 2006},
                    "body_styles": ["Single Cab", "Super Cab", "Crew Cab"],
                    "summary": "1.8L/2.0L/2.6L petrol, 2.5L Turbo Diesel, dual-range 4WD, succeeded by the Ranger."
                }
            ]
        },
        {
            "model_slug": "ranger",
            "name": "Ford Ranger",
            "vehicle_type": "Ute / Cab Chassis",
            "segment": "Mid-size Pick-up",
            "years_sold_au": {"start": 2006, "end": "Present"},
            "locally_built": False,
            "overview": "Australia's best-selling vehicle and Ford Australia's engineering masterpiece. Designed, engineered, and tested in Victoria for global markets, boasting unmatched capability and the high-speed off-road Raptor.",
            "generations": [
                {
                    "series_code": "PJ-PK",
                    "generation_name": "Ranger PJ & PK Series",
                    "years": {"start": 2006, "end": 2011},
                    "body_styles": ["Single Cab", "Super Cab", "Double Cab"],
                    "summary": "2.5L and 3.0L Duratorq TDCi common-rail turbodiesels; 3.0-tonne towing; XL and XLT."
                },
                {
                    "series_code": "PX",
                    "generation_name": "Ranger T6 Platform (PX I, II, III)",
                    "years": {"start": 2011, "end": 2022},
                    "body_styles": ["Single Cab", "Super Cab", "Double Cab"],
                    "summary": "Designed in Australia; 3.2L 5-cylinder TDCi (470Nm), 2.0L Bi-Turbo EcoBlue (500Nm, 10-speed auto), 3.5t towing, Ranger Raptor with Fox racing shocks."
                },
                {
                    "series_code": "PY",
                    "generation_name": "Next-Gen Ranger (PY)",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["Single Cab", "Super Cab", "Double Cab"],
                    "summary": "Australia's #1 selling vehicle. 3.0L V6 Turbo Diesel (184kW/600Nm) and Raptor with 292kW twin-turbo 3.0L V6 EcoBoost."
                }
            ]
        },
        {
            "model_slug": "transit",
            "name": "Ford Transit",
            "vehicle_type": "Commercial Van / Minibus / Cab Chassis",
            "segment": "Large Commercial Van",
            "years_sold_au": {"start": 1966, "end": "Present"},
            "locally_built": True,
            "overview": "The global gold standard of commercial vans. Assembled locally at Homebush and Broadmeadows with local Falcon sixes before transitioning to European imports and Transit Custom.",
            "generations": [
                {
                    "series_code": "Mk-I-Modern",
                    "generation_name": "Transit Mark I to V363 & Custom",
                    "years": {"start": 1966, "end": "Present"},
                    "body_styles": ["Van", "Cab Chassis", "Minibus"],
                    "summary": "From locally-built Falcon 3.3L/4.1L inline-six work vans to modern 2.0L EcoBlue diesels and electric E-Transit."
                }
            ]
        }
    ]
}
