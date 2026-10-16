"""
Comprehensive metadata and complete model catalogs for HSV, HDT, FPV, Lightburn,
Bolwell, Goggomobil Dart, Giocattolo, OKA, and Brabham.
"""
from typing import Any, Dict

ICONS_MAKES_DATA: Dict[str, Any] = {
    "hsv": {
        "make_slug": "hsv",
        "name": "Holden Special Vehicles (HSV)",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 1987, "end": 2020},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Holden Special Vehicles (HSV) was established in 1987 in Clayton, Victoria as a high-performance joint venture between General Motors-Holden and Scottish racing icon Tom Walkinshaw (Tom Walkinshaw Racing). Born from the ashes of Holden's split with Peter Brock's HDT, HSV elevated Australian muscle cars to world-class engineering standards. Over three decades, HSV developed legendary performance nameplates including the ClubSport, GTS, Senator, and Maloo ute. From the wild aerodynamic composite aero of the 1988 VL Walkinshaw Group A SV to the fire-breathing 375kW 7.0L W427 and the pinnacle 2017 GTSR W1 (474kW supercharged dry-sump LS9), HSV built Australia's most sought-after and collectible high-performance road and track weapons.",
        "australian_history": "Following GM-Holden's public fallout with Peter Brock in February 1987 over the Energy Polarizer and Director, Holden formed a joint venture with Tom Walkinshaw Racing (TWR) to establish Holden Special Vehicles (HSV) at Cross Street, Brookvale, quickly relocating to Clayton, Victoria under managing director John Crennan. HSV's inaugural project was the 1988 VL SS Group A SV ('Walkinshaw'), built to homologate Holden's fuel-injected 5.0L V8 for Group A touring car racing. With its radical wind-tunnel-designed aerodynamic body kit and twin-throttle-body EFI engine producing 180kW, the Walkinshaw won the 1990 Bathurst 1000 with Allan Grice and Win Percy.\n\nIn 1990, HSV introduced the ClubSport with the VN series—a badge that would become HSV's core breadwinner. The 1992 VP GTS debuted four-bolt mains and independent rear suspension, while the 1994 VR GTS introduced the 215kW Harrop-developed 5.7L 'Stroker' V8. In 1996, HSV released the outrageous VS GTS-R in 'XU3 Yellah' with carbon-fibre wing and blueprint engine option. The 1999 VT Series II marked a technological revolution with the introduction of the all-alloy Gen III LS1 5.7L Chevrolet V8, followed in 2000 by the bespoke 300kW Callaway-tuned C4B V8 in the GTS.\n\nIn 2006, HSV released the E-Series on Holden's new Zeta platform, pioneering Magnetic Ride Control (MRC) active dampers and the LS2 6.0L / LS3 6.2L V8s. To mark HSV's 20th anniversary in 2008, HSV shoehorned the Corvette Z06's hand-built 7.0-litre LS7 V8 into the Commodore body to create the 375kW HSV W427. In 2013, the GEN-F series brought the supercharged 6.2L LSA V8 (430kW/740Nm) to the GTS. HSV saved its finest hour for the closure of Australian manufacturing in 2017 with the GTSR W1: powered by the Corvette ZR1's 474kW (636 bhp) supercharged 6.2L dry-sump LS9 V8, mated to a Tremec TR-6060 close-ratio manual and bespoke Australian Supashock racing dampers, only 275 were built, instantly becoming Australia's ultimate muscle car icon. Following factory closure, HSV evolved into Walkinshaw Automotive Group.",
        "models_catalog": [
            {
                "model_slug": "vl-walkinshaw",
                "name": "HSV VL SS Group A SV",
                "vehicle_type": "Sedan",
                "segment": "Homologation Special / Muscle Car",
                "years_sold_au": {"start": 1988, "end": 1988},
                "locally_built": True,
                "overview": "The foundational car of HSV. A wild wind-tunnel-developed Group A homologation special finished in Panorama Silver with twin-throttle 5.0L V8.",
                "generations": [
                    {
                        "series_code": "VL-Group-A",
                        "generation_name": "VL SS Group A SV Walkinshaw",
                        "years": {"start": 1988, "end": 1988},
                        "body_styles": ["4-door sedan"],
                        "summary": "5.0L V8 (180kW/380Nm), twin throttle-body intake, T5 5-speed manual, 750 homologation units produced; won 1990 Bathurst 1000."
                    }
                ]
            },
            {
                "model_slug": "clubsport-gts",
                "name": "HSV ClubSport & GTS",
                "vehicle_type": "Sedan",
                "segment": "Performance / Muscle Car",
                "years_sold_au": {"start": 1990, "end": 2017},
                "locally_built": True,
                "overview": "The core of the HSV legend. Spanning VN through GEN-F2, from the early 5.0L Holden V8s to the Callaway C4B, LS3, and the supercharged 474kW GTSR W1.",
                "generations": [
                    {
                        "series_code": "VN-VP",
                        "generation_name": "VN & VP Series (ClubSport & GTS)",
                        "years": {"start": 1990, "end": 1993},
                        "body_styles": ["4-door performance sedan"],
                        "summary": "Holden 5.0L EFI V8 (180kW VN ClubSport; 200kW VP GTS with 4-bolt mains and IRS)."
                    },
                    {
                        "series_code": "VR-VS",
                        "generation_name": "VR & VS Series (ClubSport, GTS, GTS-R)",
                        "years": {"start": 1993, "end": 1997},
                        "body_styles": ["4-door performance sedan"],
                        "summary": "185kW 5.0L and 215kW 5.7L Harrop Stroker V8; iconic 1996 VS GTS-R in XU-3 Yellah."
                    },
                    {
                        "series_code": "VT-VX",
                        "generation_name": "VT & VX Series (LS1 & Callaway C4B)",
                        "years": {"start": 1997, "end": 2002},
                        "body_styles": ["4-door performance sedan"],
                        "summary": "Transition to Gen III 5.7L LS1 V8 (250kW-255kW) and bespoke 300kW Callaway C4B GTS."
                    },
                    {
                        "series_code": "VY-VZ",
                        "generation_name": "VY & VZ Series (ClubSport & GTS)",
                        "years": {"start": 2002, "end": 2006},
                        "body_styles": ["4-door performance sedan"],
                        "summary": "285kW LS1 V8 and 297kW 6.0L LS2 V8; AP Racing brakes."
                    },
                    {
                        "series_code": "E-Series",
                        "generation_name": "E-Series (E1, E2, E3)",
                        "years": {"start": 2006, "end": 2013},
                        "body_styles": ["4-door performance sedan"],
                        "summary": "Zeta platform; 307kW LS2 and 317kW/325kW LS3 V8s; Magnetic Ride Control (MRC) suspension."
                    },
                    {
                        "series_code": "GEN-F",
                        "generation_name": "GEN-F & GEN-F2 (GTS, GTSR, W1)",
                        "years": {"start": 2013, "end": 2017},
                        "body_styles": ["4-door performance sedan"],
                        "summary": "Supercharged 6.2L LSA V8 (430kW/740Nm), GTSR (435kW), and the ultimate GTSR W1 with 474kW LS9 dry-sump V8 and Supashock dampers."
                    }
                ]
            },
            {
                "model_slug": "senator",
                "name": "HSV Senator",
                "vehicle_type": "Sedan",
                "segment": "Prestige Performance",
                "years_sold_au": {"start": 1992, "end": 2017},
                "locally_built": True,
                "overview": "HSV's executive express, combining luxury appointments, premium leather, discreet aerodynamic styling, and potent V8 powertrains.",
                "generations": [
                    {
                        "series_code": "VP-GEN-F",
                        "generation_name": "Senator Evolution (VP through GEN-F2)",
                        "years": {"start": 1992, "end": 2017},
                        "body_styles": ["4-door luxury sports sedan"],
                        "summary": "Senator 5000i, Senator Signature, 5.7L Stroker, LS1, LS2, LS3, and final supercharged 400kW Senator Signature LSA."
                    }
                ]
            },
            {
                "model_slug": "maloo",
                "name": "HSV Maloo",
                "vehicle_type": "Coupe Utility",
                "segment": "Performance Ute",
                "years_sold_au": {"start": 1990, "end": 2017},
                "locally_built": True,
                "overview": "The world's fastest production utility. Named from the Indigenous Australian word for 'thunder', the Maloo set Guinness World Records for ute speed.",
                "generations": [
                    {
                        "series_code": "VG-GEN-F",
                        "generation_name": "Maloo Evolution (VG through GEN-F2)",
                        "years": {"start": 1990, "end": 2017},
                        "body_styles": ["2-door coupe utility"],
                        "summary": "From 180kW VG Maloo to 400kW Maloo R8 LSA and ultra-limited GEN-F2 GTSR Maloo."
                    }
                ]
            },
            {
                "model_slug": "grange",
                "name": "HSV Grange",
                "vehicle_type": "Sedan",
                "segment": "Long-Wheelbase Luxury Performance",
                "years_sold_au": {"start": 1996, "end": 2016},
                "locally_built": True,
                "overview": "Flagship performance limousine built on the long-wheelbase Statesman and Caprice bodies, named after Penfolds Grange Hermitage.",
                "generations": [
                    {
                        "series_code": "VS-WN",
                        "generation_name": "Grange (VS, WH, WK, WL, WM, WN)",
                        "years": {"start": 1996, "end": 2016},
                        "body_styles": ["4-door long-wheelbase sedan"],
                        "summary": "215kW 5.7L Stroker, LS1 250kW, LS2 297kW, and WM/WN 325kW/340kW LS3 with Magnetic Ride Control."
                    }
                ]
            },
            {
                "model_slug": "coupe-gto-gts",
                "name": "HSV Coupe GTO & Coupe GTS",
                "vehicle_type": "Coupe",
                "segment": "Sports Coupe / Muscle Car",
                "years_sold_au": {"start": 2001, "end": 2006},
                "locally_built": True,
                "overview": "Sensational performance coupes crafted on the third-generation Holden Monaro body, featuring aggressive styling and up to 300kW Callaway C4B power.",
                "generations": [
                    {
                        "series_code": "V2-VZ",
                        "generation_name": "Coupe GTO & Coupe GTS",
                        "years": {"start": 2001, "end": 2006},
                        "body_styles": ["2-door coupe"],
                        "summary": "GTO (255kW-285kW LS1, 297kW LS2) and Coupe GTS (300kW Callaway C4B V8, AP Racing brakes)."
                    }
                ]
            },
            {
                "model_slug": "avalanche",
                "name": "HSV Avalanche & Avalanche XUV",
                "vehicle_type": "AWD Wagon / Dual-Cab Ute",
                "segment": "Performance AWD Crossover",
                "years_sold_au": {"start": 2003, "end": 2005},
                "locally_built": True,
                "overview": "High-performance all-wheel-drive crossover wagon and XUV dual-cab utility based on the Adventra/Crewman platform with Cross Trac AWD and 5.7L LS1 V8.",
                "generations": [
                    {
                        "series_code": "VY-VZ",
                        "generation_name": "Avalanche Series",
                        "years": {"start": 2003, "end": 2005},
                        "body_styles": ["5-door AWD wagon", "4-door dual-cab AWD utility (XUV)"],
                        "summary": "5.7L LS1 V8 (270kW/475Nm), permanent Cross Trac AWD with 62% rear bias, 18-inch wheels, AP Racing brakes."
                    }
                ]
            },
            {
                "model_slug": "w427",
                "name": "HSV W427",
                "vehicle_type": "Sedan",
                "segment": "Supercar / Limited Edition",
                "years_sold_au": {"start": 2008, "end": 2009},
                "locally_built": True,
                "overview": "HSV's 20th anniversary masterpiece. Hand-assembled at Clayton with the Corvette Z06's dry-sump 7.0-litre (427ci) LS7 V8, producing 375kW and 640Nm.",
                "generations": [
                    {
                        "series_code": "E-Series",
                        "generation_name": "HSV W427",
                        "years": {"start": 2008, "end": 2009},
                        "body_styles": ["4-door supercar sedan"],
                        "summary": "7.0L LS7 V8 (375kW/640Nm), dry sump lubrication, Tremec TR-6060 manual, 6-piston AP brakes, 137 units produced."
                    }
                ]
            },
            {
                "model_slug": "sportscat",
                "name": "HSV Colorado SportsCat",
                "vehicle_type": "Ute",
                "segment": "Performance 4WD Dual-Cab",
                "years_sold_au": {"start": 2018, "end": 2020},
                "locally_built": True,
                "overview": "Re-engineered Holden Colorado dual-cab 4WD featuring MTV dampers or Supashock suspension, Cooper Zeon tyres, and AP Racing 4-piston brakes.",
                "generations": [
                    {
                        "series_code": "RG",
                        "generation_name": "SportsCat & SportsCat+",
                        "years": {"start": 2018, "end": 2020},
                        "body_styles": ["4-door dual-cab 4WD"],
                        "summary": "2.8L Duramax turbo-diesel (147kW/500Nm), Supashock dampers, de-coupling rear anti-roll bar, AP Racing front brakes."
                    }
                ]
            }
        ]
    },
    "hdt": {
        "make_slug": "hdt",
        "name": "Holden Dealer Team (HDT)",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 1980, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Holden Dealer Team (HDT) Special Vehicles was established in 1980 by nine-time Bathurst champion Peter Brock at 124 Bertie Street, Port Melbourne. When Holden withdrew factory motorsport funding in 1979, Brock purchased the team with financial backing from a coalition of Holden dealers. HDT transformed showroom Commodores into bespoke high-performance road cars with hand-assembled blueprint V8 engines, Bilstein suspension, Scheel sports seats, Momo steering wheels, and wind-tunnel aero bodykits. HDT created Australia's most revered homologation muscle car—the 1985 VK SS Group A 'Blue Meanie'—alongside the VC Brock Commodore, VH Group 3, and VL Group A before Brock's split with Holden in 1987. Today, HDT builds retro heritage editions.",
        "australian_history": "The Holden Dealer Team originated in 1969 when Harry Firth created a semi-works team for Holden. Peter Brock joined in 1969, scoring his first Bathurst win in an LJ Torana GTR XU-1 in 1972. When GM-Holden ended direct factory backing in 1979, Brock negotiated with the Holden Dealer Network to acquire the team, launching HDT Special Vehicles in 1980.\n\nHDT's first road car, the 1980 VC HDT Commodore, was an instant triumph: 500 numbered cars in Firethorn Red, Palais White, and Tuxedo Black with 5.0L (160kW) and 4.2L V8s, Irmscher wheels, and Bilstein dampers. This was followed by the VH Group 1, Group 2, and Group 3 (with Brock's signature high-output 180kW 5.0L V8). In 1983, HDT expanded into luxury with the WB Magnum Statesman.\n\nIn 1985, to homologate the Commodore for international Group A touring car rules, HDT produced 500 examples of the VK SS Group A. Painted exclusively in Formula Blue, the 'Blue Meanie' featured a de-stroked 4.9-litre (4987cc) V8 with Crane cam, roller rockers, double-row timing chain, and distinctive white Aero wheels. In 1986, HDT followed with the VL SS Group A, creating the famous 'Plus Pack'.\n\nHowever, in 1986-1987, Brock championed the 'Energy Polarizer'—a small resin-filled box containing crystals and magnets that Brock claimed realigned molecular structures to improve ride and performance—and demanded Holden endorse it on the new HDT Director luxury car. When Holden technical director Ray Borrett tested the car and discovered unauthorized rear suspension modifications and no scientific validity to the Polarizer, Holden formally severed all ties with HDT in February 1987. The Brock HDT era ended, but the marque was later resurrected by Peter Champion and operates today building heritage Brock tributes.",
        "models_catalog": [
            {
                "model_slug": "vc-brock-commodore",
                "name": "HDT VC Brock Commodore",
                "vehicle_type": "Sedan",
                "segment": "Performance Muscle Car",
                "years_sold_au": {"start": 1980, "end": 1980},
                "locally_built": True,
                "overview": "The original Brock road car. 500 individually numbered cars in Firethorn Red, Palais White, and Tuxedo Black with 160kW 5.0L V8 and Irmscher alloys.",
                "generations": [
                    {
                        "series_code": "VC-HDT",
                        "generation_name": "VC Brock Commodore",
                        "years": {"start": 1980, "end": 1980},
                        "body_styles": ["4-door sedan"],
                        "summary": "5.0L 308 V8 (160kW) or 4.2L V8 (115kW), heavy-duty TH350 auto or 4-speed manual, Bilstein suspension, Scheel seats."
                    }
                ]
            },
            {
                "model_slug": "vh-group-3",
                "name": "HDT VH SS Group 1, 2 & 3",
                "vehicle_type": "Sedan",
                "segment": "Performance Muscle Car",
                "years_sold_au": {"start": 1981, "end": 1984},
                "locally_built": True,
                "overview": "The car that defined 1980s Australian street performance, culminating in the Group 3 with Brock's modified 180kW blueprint 5.0L V8.",
                "generations": [
                    {
                        "series_code": "VH-HDT",
                        "generation_name": "VH SS Group 1 / 2 / 3",
                        "years": {"start": 1981, "end": 1984},
                        "body_styles": ["4-door sedan"],
                        "summary": "High-compression B-cast cylinder heads, port-matched intake, Crane cam, 180kW/430Nm, Irmscher wheels, full aerodynamic skirts."
                    }
                ]
            },
            {
                "model_slug": "vk-group-a",
                "name": "HDT VK SS Group A ('Blue Meanie')",
                "vehicle_type": "Sedan",
                "segment": "Homologation Special / Muscle Car",
                "years_sold_au": {"start": 1985, "end": 1985},
                "locally_built": True,
                "overview": "Australia's most iconic homologation muscle car. 500 built in Formula Blue with 4.9L V8, Crane cam, roller rockers, and white 16-inch Aero wheels.",
                "generations": [
                    {
                        "series_code": "VK-Group-A",
                        "generation_name": "VK SS Group A & Group 3",
                        "years": {"start": 1985, "end": 1985},
                        "body_styles": ["4-door sedan"],
                        "summary": "4,987cc V8 (196kW/418Nm) homologated under 5,000cc; M21 4-speed manual, Formula Blue paint, Scheel velour interior."
                    }
                ]
            },
            {
                "model_slug": "vl-group-a",
                "name": "HDT VL SS Group A & Director",
                "vehicle_type": "Sedan",
                "segment": "Performance / Luxury Muscle",
                "years_sold_au": {"start": 1986, "end": 1988},
                "locally_built": True,
                "overview": "The final factory-supported Brock Commodores (VL Group A in Permanent Red) and the infamous, opulent Director that triggered the split with Holden.",
                "generations": [
                    {
                        "series_code": "VL-HDT",
                        "generation_name": "VL Group A, Plus Pack & Director",
                        "years": {"start": 1986, "end": 1988},
                        "body_styles": ["4-door sedan"],
                        "summary": "4.9L V8 (137kW-168kW), Plus Pack with revised suspension, and the bespoke Director luxury sedan with Corvette IRS."
                    }
                ]
            },
            {
                "model_slug": "magnum",
                "name": "HDT Magnum",
                "vehicle_type": "Sedan / Utility",
                "segment": "Luxury Performance",
                "years_sold_au": {"start": 1983, "end": 1985},
                "locally_built": True,
                "overview": "HDT's luxurious grand-touring adaptation of the WB Statesman de Ville and WB utility, featuring Group 3 V8 power and high-speed touring stability.",
                "generations": [
                    {
                        "series_code": "WB-Magnum",
                        "generation_name": "WB HDT Magnum",
                        "years": {"start": 1983, "end": 1985},
                        "body_styles": ["4-door long-wheelbase sedan", "Coupe utility"],
                        "summary": "5.0L 308 V8 (188kW), TH350 auto, Bilstein suspension, 15-inch Momo wheels, Connolly leather or velour trim."
                    }
                ]
            },
            {
                "model_slug": "monza",
                "name": "HDT Monza",
                "vehicle_type": "Coupe",
                "segment": "Grand Tourer Coupe",
                "years_sold_au": {"start": 1982, "end": 1985},
                "locally_built": True,
                "overview": "Peter Brock's concept to produce a European grand tourer in Australia, transplanting Holden 5.0L V8s and Supra 5-speed gearboxes into Opel Monza fastback coupes.",
                "generations": [
                    {
                        "series_code": "Monza",
                        "generation_name": "HDT Monza Coupe",
                        "years": {"start": 1982, "end": 1985},
                        "body_styles": ["2-door fastback coupe"],
                        "summary": "Opel Monza bodyshell, Holden 5.0L V8 (180kW), 5-speed manual, independent rear suspension, only ~4 built."
                    }
                ]
            },
            {
                "model_slug": "heritage-retro",
                "name": "HDT Heritage & Retro Series",
                "vehicle_type": "Sedan / Ute",
                "segment": "Retro Muscle Car",
                "years_sold_au": {"start": 2008, "end": "Present"},
                "locally_built": True,
                "overview": "Modern bespoke tribute vehicles built on VE and VF Commodore platforms recreating iconic VC, VH, and VK Blue Meanie designs with 6.0L/6.2L V8 power.",
                "generations": [
                    {
                        "series_code": "VE-VF-Retro",
                        "generation_name": "HDT Retro Series",
                        "years": {"start": 2008, "end": "Present"},
                        "body_styles": ["Sedan", "Ute"],
                        "summary": "Modern retro builds with VK aero bodywork, white Aero wheels, Harrop superchargers producing over 450kW."
                    }
                ]
            }
        ]
    },
    "fpv": {
        "make_slug": "fpv",
        "name": "Ford Performance Vehicles (FPV)",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 2002, "end": 2014},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Ford Performance Vehicles (FPV) was established in 2002 in Campbellfield, Victoria as a high-performance joint venture between Ford Australia and British racing powerhouse Prodrive, succeeding Tickford Vehicle Engineering (TVE). FPV engineered the most devastating performance Falcons ever created. FPV became renowned for its hand-assembled 'Boss' quad-cam 32-valve 5.4-litre V8s (Boss 290, 302, 315) and the revolutionary turbocharged 'Barra' 4.0-litre twin-cam six in the F6 Typhoon and Tornado (yielding a massive 565Nm of torque). In 2010, FPV introduced the Australian-developed 'Miami' 5.0-litre supercharged V8, crowning its legacy with the limited-edition 2014 FG GT-F 351 (capable of over 400kW on overboost), before operations concluded in late 2014.",
        "australian_history": "FPV was born from the rich heritage of Tickford Vehicle Engineering (TVE), established in 1991 to create the Falcon XR6 and XR8. In 2002, Ford and Prodrive established Ford Performance Vehicles at Campbellfield, directly opposite Ford's main plant. Under chief engineer Bryan Mears and Prodrive boss David Flint, FPV launched the BA GT and GT-P in early 2003, featuring the Boss 290—a unique Australian creation pairing an American modular 5.4L cast-iron block with quad-cam 32-valve cylinder heads from the Mustang Cobra R.\n\nIn late 2004, FPV launched the F6 Typhoon sedan and F6 Tornado ute, powered by a high-boost version of the Barra 4.0-litre inline-six developing 270kW and 550Nm of torque. The F6 out-accelerated contemporary V8s and earned legendary status as one of Australia's greatest performance engines.\n\nIn 2008, the FG series introduced the Boss 315 V8 and the F6 310 (310kW/565Nm) featuring an enormous front-mount intercooler and Garrett GT3576R turbocharger. In late 2010, under 'Project Panther', FPV invested $40 million to develop the supercharged 'Miami' 5.0-litre V8 based on Ford's Coyote engine, incorporating a top-mounted Harrop HTV 1900 supercharger with integrated water-to-air intercooling. In 2012, Ford bought out Prodrive's stake in FPV, integrating production directly into Ford Broadmeadows. FPV signed off in June 2014 with the GT-F 351 (351kW / 570Nm, paying tribute to the 351 Cleveland), with 500 numbered sedans built for Australia.",
        "models_catalog": [
            {
                "model_slug": "gt-f6",
                "name": "FPV GT & F6",
                "vehicle_type": "Sedan",
                "segment": "Performance / Muscle Car",
                "years_sold_au": {"start": 2003, "end": 2014},
                "locally_built": True,
                "overview": "The twin pillars of FPV: the thunderous quad-cam and supercharged V8 GT (GT, GT-P, GT-E, GT-F 351) and the devastating Barra turbo F6 Typhoon.",
                "generations": [
                    {
                        "series_code": "BA",
                        "generation_name": "BA Series (Boss 290 & F6 Typhoon)",
                        "years": {"start": 2003, "end": 2005},
                        "body_styles": ["4-door sedan"],
                        "summary": "Boss 290 5.4L quad-cam V8 (290kW/520Nm), Tremec T56 6-speed; F6 Typhoon with Barra 270T (270kW/550Nm)."
                    },
                    {
                        "series_code": "BF",
                        "generation_name": "BF & BF Mk II Series",
                        "years": {"start": 2005, "end": 2008},
                        "body_styles": ["4-door sedan"],
                        "summary": "ZF 6-speed automatic transmission, Brembo 6-piston brakes, Force 6 and Force 8 luxury executive models."
                    },
                    {
                        "series_code": "FG-I",
                        "generation_name": "FG Series I (Boss 315 & F6 310)",
                        "years": {"start": 2008, "end": 2010},
                        "body_styles": ["4-door sedan"],
                        "summary": "Boss 315 V8 (315kW/551Nm) and legendary F6 (310kW/565Nm, 0-100 in 4.9s)."
                    },
                    {
                        "series_code": "FG-II",
                        "generation_name": "FG Series II & GT-F 351 (Supercharged Miami V8)",
                        "years": {"start": 2010, "end": 2014},
                        "body_styles": ["4-door sedan"],
                        "summary": "Supercharged 5.0L Miami V8 (335kW/570Nm), launch control, and final GT-F 351 with over 400kW transient overboost."
                    }
                ]
            },
            {
                "model_slug": "pursuit-super-pursuit",
                "name": "FPV Pursuit & Super Pursuit",
                "vehicle_type": "Coupe Utility",
                "segment": "Performance Utility",
                "years_sold_au": {"start": 2003, "end": 2014},
                "locally_built": True,
                "overview": "FPV's high-performance utes packing Boss V8, supercharged Miami V8, and F6 Tornado turbo six firepower.",
                "generations": [
                    {
                        "series_code": "BA-FG",
                        "generation_name": "FPV Ute Evolution (BA through FG)",
                        "years": {"start": 2003, "end": 2014},
                        "body_styles": ["2-door coupe utility"],
                        "summary": "Pursuit, Super Pursuit, and F6 Tornado; leaf-sprung performance workhorses packing up to 335kW."
                    }
                ]
            },
            {
                "model_slug": "f6x",
                "name": "FPV F6X",
                "vehicle_type": "SUV",
                "segment": "High-Performance SUV",
                "years_sold_au": {"start": 2008, "end": 2009},
                "locally_built": True,
                "overview": "Australia's fastest SUV at launch. Engineered from the Ford Territory with the 270kW Barra Turbo six, full-time AWD, and Brembo six-piston brakes.",
                "generations": [
                    {
                        "series_code": "SY",
                        "generation_name": "FPV F6X 270",
                        "years": {"start": 2008, "end": 2009},
                        "body_styles": ["5-door performance SUV"],
                        "summary": "Barra 270T 4.0L Turbo I6 (270kW/550Nm), full-time AWD, ZF 6-speed auto, Brembo brakes, 0-100 in 5.9s; 229 units built."
                    }
                ]
            },
            {
                "model_slug": "gs",
                "name": "FPV GS",
                "vehicle_type": "Sedan / Utility",
                "segment": "Performance Muscle Car",
                "years_sold_au": {"start": 2009, "end": 2014},
                "locally_built": True,
                "overview": "Accessible FPV entry point introduced in 2009 with Boss 302 V8 and upgraded in 2010 to a 302kW version of the supercharged Miami 5.0L V8.",
                "generations": [
                    {
                        "series_code": "FG",
                        "generation_name": "FPV GS Sedan & Ute",
                        "years": {"start": 2009, "end": 2014},
                        "body_styles": ["4-door sedan", "2-door coupe utility"],
                        "summary": "Boss 302 (302kW) followed by supercharged Miami 5.0L V8 (302kW/540Nm), historic GS side stripes."
                    }
                ]
            }
        ]
    },
    "lightburn": {
        "make_slug": "lightburn",
        "name": "Lightburn",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 1963, "end": 1966},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Lightburn & Co. was an Adelaide-based manufacturing firm founded by Harold Lightburn, famed across Australia for building concrete mixers, washing machines, and fiberglass powerboats. In 1963, Lightburn made an ambitious leap into automobile manufacturing with the Zeta, a fiberglass-bodied microcar produced in Camden Park, South Australia. Powered by an air-cooled British Villiers 324cc 2-stroke motorcycle engine driving the front wheels, the Zeta featured a motorcycle-style sequential gearbox and no reverse gear—the driver stopped the engine and restarted it running backwards. Lightburn also produced the attractive Zeta Sports roadster and a commercial Zeta Utility before production ceased in 1966 after approximately 400 vehicles.",
        "australian_history": "Harold Lightburn had built an industrial empire in South Australia producing cement mixers, industrial jacks, and washing machines. Convinced that the suburban Australian family needed an affordable, corrosion-proof second car, Lightburn invested in tooling to build a fiberglass-bodied microcar at Camden Park, Adelaide.\n\nLaunched in 1963, the Zeta Sedan sold for 598 pounds, undercutting the BMC Mini. Its body was molded from reinforced polyester fiberglass, impervious to rust. The drivetrain was a 324cc Villiers 2-stroke twin-cylinder engine producing just 12 kW (16.5 bhp), mounted to an unsynchronized 4-speed sequential dog clutch transaxle. Remarkably, the car lacked an exterior boot lid—luggage had to be loaded through the front doors over the rear bench seat. Backing up required shutting down the engine and using a dual-contact ignition key to start the Villiers twin in reverse rotation.\n\nIn 1964, Lightburn revealed the Zeta Sports, an attractive fiberglass roadster styled after the British Frisky Sprint, featuring bumperless sports styling, Michelin X tyres, and an upgraded 498cc Sachs twin-cylinder engine with a 4-speed gearbox with real reverse. Lightburn also developed the Zeta Utility for light commercial duties. However, Australians preferred larger second-hand Holdens or modern Minis, and the Zeta's high interior noise and quirky mechanicals restricted sales. Production ended in 1966 with only ~363 sedans and utilities and 28 Zeta Sports ever built.",
        "models_catalog": [
            {
                "model_slug": "zeta-sedan",
                "name": "Lightburn Zeta Sedan",
                "vehicle_type": "Microcar",
                "segment": "Micro / City Car",
                "years_sold_au": {"start": 1963, "end": 1965},
                "locally_built": True,
                "overview": "Fiberglass-bodied Australian microcar powered by a front-mounted 324cc Villiers two-stroke twin with reversible ignition starter.",
                "generations": [
                    {
                        "series_code": "Zeta-Sedan",
                        "generation_name": "Zeta Sedan",
                        "years": {"start": 1963, "end": 1965},
                        "body_styles": ["2-door sedan"],
                        "summary": "Villiers 324cc 2-stroke twin (12kW/16.5 hp), front-wheel drive, independent rubber suspension, rust-proof fiberglass body."
                    }
                ]
            },
            {
                "model_slug": "zeta-sports",
                "name": "Lightburn Zeta Sports",
                "vehicle_type": "Roadster",
                "segment": "Micro Sports",
                "years_sold_au": {"start": 1964, "end": 1965},
                "locally_built": True,
                "overview": "Rare and charming fiberglass roadster with FMR/Sachs 498cc twin-cylinder engine and Frisky-inspired body lines; only 28 produced.",
                "generations": [
                    {
                        "series_code": "Zeta-Sports",
                        "generation_name": "Zeta Sports Roadster",
                        "years": {"start": 1964, "end": 1965},
                        "body_styles": ["2-door open roadster"],
                        "summary": "Fichtel & Sachs 498cc 2-stroke twin (15.5kW/21 hp), 4-speed manual with true reverse, 125 km/h top speed."
                    }
                ]
            },
            {
                "model_slug": "zeta-utility",
                "name": "Lightburn Zeta Utility",
                "vehicle_type": "Micro Utility",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 1964, "end": 1965},
                "locally_built": True,
                "overview": "Open-tray micro utility variant of the Zeta built for local councils and light delivery duties.",
                "generations": [
                    {
                        "series_code": "Zeta-Ute",
                        "generation_name": "Zeta Utility",
                        "years": {"start": 1964, "end": 1965},
                        "body_styles": ["2-door micro utility"],
                        "summary": "324cc Villiers engine, open rear load bed, minimal curb weight, highly economical commercial runner."
                    }
                ]
            }
        ]
    },
    "bolwell": {
        "make_slug": "bolwell",
        "name": "Bolwell",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 1962, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Bolwell Cars was founded in Melbourne, Victoria in 1962 by brothers Graeme and Campbell Bolwell. Bolwell is Australia's most enduring and respected bespoke sports car manufacturer. Beginning with fiberglass kit sports cars (Mk IV and Mk VII), Bolwell achieved international acclaim in 1970 with the Nagari (Mk VIII), a fully productionized road-legal supercar featuring a steel backbone chassis, fiberglass body, and Ford 302ci/351ci V8 power. In the 21st century, Bolwell leveraged advanced aerospace vacuum-infused carbon composites to produce the Nagari 300 and Nagari 500 mid-engine supercars.",
        "australian_history": "Campbell Bolwell built his first special in 1962, founding Bolwell Cars in Melbourne. The Mk IV and gullwing Mk VII established Bolwell as masters of fiberglass styling and composites. In 1969, Graeme Bolwell returned from a stint working with Colin Chapman at Lotus in England, bringing advanced chassis engineering expertise back to Australia.\n\nIn 1970, Bolwell unveiled the Nagari (Mk VIII)—from an Aboriginal word meaning 'flowing'. Unlike kit predecessors, the Nagari was sold as a fully built factory production car from Bolwell's factory in Mordialloc, Victoria. Featuring a rigid Y-shaped steel backbone chassis, Austin 1800 front suspension uprights, and Ford Falcon mechanicals (including 302ci Windsor and 351ci Cleveland V8s), the Nagari weighed just 1,040 kg and hit 100 km/h in under 6 seconds, out-accelerating contemporary Ferraris and Porsches. Bolwell built 100 coupes and 27 convertibles before production ended in 1974 due to incoming ADR safety and emission compliance costs.\n\nBolwell diversified into commercial composites, supplying fiberglass trucks and train cabs. In 1979, they introduced the mid-engine Ikara kit car. In 2008, Campbell Bolwell revived the marque with the Nagari 300, a carbon-fibre monocoque supercar powered by a 220kW 3.5L quad-cam Toyota V6, later followed by the supercharged Nagari 500 with a 375kW Chevrolet LS3 V8.",
        "models_catalog": [
            {
                "model_slug": "mk-iv",
                "name": "Bolwell Mk IV",
                "vehicle_type": "Sports Coupe / Roadster",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1962, "end": 1964},
                "locally_built": True,
                "overview": "The earliest commercial Bolwell sports car, offered as a fiberglass body-chassis unit accepting Ford Ten or Cortina running gear.",
                "generations": [
                    {
                        "series_code": "Mk-IV",
                        "generation_name": "Bolwell Mk IV",
                        "years": {"start": 1962, "end": 1964},
                        "body_styles": ["Coupe", "Roadster"],
                        "summary": "Lightweight tubular spaceframe with fiberglass shell; around 50 produced."
                    }
                ]
            },
            {
                "model_slug": "mk-vii",
                "name": "Bolwell Mk VII",
                "vehicle_type": "Coupe",
                "segment": "Sports Coupe",
                "years_sold_au": {"start": 1967, "end": 1971},
                "locally_built": True,
                "overview": "Sleek fastback sports coupe based on Holden mechanicals (186 Red motor), setting the stage for the Nagari.",
                "generations": [
                    {
                        "series_code": "Mk-VII",
                        "generation_name": "Bolwell Mk VII",
                        "years": {"start": 1967, "end": 1971},
                        "body_styles": ["2-door fastback coupe"],
                        "summary": "Holden 186/186S six-cylinder engine, HR front suspension; over 400 kits sold."
                    }
                ]
            },
            {
                "model_slug": "nagari-mk-viii",
                "name": "Bolwell Nagari (Mk VIII)",
                "vehicle_type": "Sports Coupe / Convertible",
                "segment": "Supercar / V8 Sports",
                "years_sold_au": {"start": 1970, "end": 1974},
                "locally_built": True,
                "overview": "Australia's legendary factory-built V8 sports car. Steel backbone chassis, fiberglass body, and Ford 302/351 V8 power, achieving 0-100 km/h in 5.8 seconds.",
                "generations": [
                    {
                        "series_code": "Mk-VIII",
                        "generation_name": "Nagari Mk VIII",
                        "years": {"start": 1970, "end": 1974},
                        "body_styles": ["2-door coupe", "2-door convertible"],
                        "summary": "Ford 302/351ci V8 (179kW-224kW), 4-speed Toploader manual, 1,040 kg curb weight; 127 units built."
                    }
                ]
            },
            {
                "model_slug": "ikara",
                "name": "Bolwell Ikara",
                "vehicle_type": "Roadster",
                "segment": "Sports Kit Car",
                "years_sold_au": {"start": 1979, "end": 1982},
                "locally_built": True,
                "overview": "Radical mid-engine open sports car utilizing a spaceframe chassis and Volkswagen Golf mechanicals.",
                "generations": [
                    {
                        "series_code": "Ikara",
                        "generation_name": "Bolwell Ikara",
                        "years": {"start": 1979, "end": 1982},
                        "body_styles": ["2-door open roadster"],
                        "summary": "1.6L VW Golf engine mounted amidships, fiberglass composite panels, 12 units produced."
                    }
                ]
            },
            {
                "model_slug": "nagari-300-500",
                "name": "Bolwell Nagari 300 / 500",
                "vehicle_type": "Coupe",
                "segment": "Supercar",
                "years_sold_au": {"start": 2008, "end": "Present"},
                "locally_built": True,
                "overview": "21st-century Australian carbon-composite supercar featuring mid-mounted 3.5L V6 or 375kW 6.2L Chevrolet LS3 V8.",
                "generations": [
                    {
                        "series_code": "Nagari-Modern",
                        "generation_name": "Nagari 300 & Nagari 500",
                        "years": {"start": 2008, "end": "Present"},
                        "body_styles": ["2-door coupe"],
                        "summary": "Carbon-kevlar monocoque, Toyota 3.5L V6 (220kW) or 375kW LS3 V8, 980 kg curb weight."
                    }
                ]
            }
        ]
    },
    "goggomobil-dart": {
        "make_slug": "goggomobil-dart",
        "name": "Buckle / Goggomobil Australia",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 1955, "end": 1962},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Buckle Motors was founded by Sydney automotive entrepreneur and racing driver Bill Buckle. To bypass steep Australian import tariffs on completed motor vehicles in the late 1950s, Buckle negotiated with Hans Glas GmbH in Germany to import rolling chassis of the Goggomobil microcar, manufacturing fiberglass sedan, coupe, and van bodies at his Punchbowl and Brookvale workshops in Sydney. In 1959, Buckle designed and released his masterpiece: the Goggomobil Dart. A doorless, two-seat aerodynamic roadster weighing only 345 kg and standing just 1.1 meters tall, the Dart was powered by a rear-mounted 300cc or 400cc air-cooled twin-cylinder two-stroke engine. The Dart achieved lasting Australian fame, becoming a beloved cultural icon celebrated for its delightful styling and timeless Yellow Pages television commercials.",
        "australian_history": "Bill Buckle was one of the true creative visionaries of Australian motoring. In 1955, he designed and constructed the Buckle 2.5 Litre coupe, a lightweight fiberglass grand tourer utilizing Ford Zephyr mechanicals that competed successfully at Mount Panorama and Australian sports car championships.\n\nSeeking a high-volume manufacturing venture, Buckle traveled to Dingolfing, West Germany in 1957 to meet Hans Glas. Australia imposed steep 65% import duties on assembled cars, but imported chassis components attracted only 7.5% duty. Buckle secured exclusive Australian rights to import Goggomobil mechanicals and set up a state-of-the-art fiberglass moulding plant in Brookvale, northern Sydney. Buckle produced hundreds of Goggomobil Sedans (Regent), Coupes (TS), and lightweight Transporter delivery vans.\n\nIn 1958, Buckle conceived an ultra-low, two-seat sports roadster on the 1,800mm Goggomobil chassis. Eschewing heavy doors that would compromise torsional rigidity, Buckle molded an ultra-lightweight one-piece fiberglass tub with scalloped sides that drivers and passengers simply stepped into. The styling featured tiny tail fins, faired-in headlamps, and a wraparound Plexiglas windscreen. Launched in 1959 as the Goggomobil Dart, it retailed for just 635 Australian pounds. Powered by a rear-mounted 293cc (15 hp) or 392cc (20 hp) twin-cylinder air-cooled two-stroke engine coupled to an innovative electric pre-selector transmission, the Dart could reach 100 km/h and offered astonishing agility. Around 700 Darts were built before production ended in 1962 as the BMC Mini arrived. Decades later, the Dart entered Australian pop culture folklore through Tommy Dyson's legendary Yellow Pages television advertisements.",
        "models_catalog": [
            {
                "model_slug": "dart",
                "name": "Goggomobil Dart",
                "vehicle_type": "Roadster",
                "segment": "Micro Sports",
                "years_sold_au": {"start": 1959, "end": 1962},
                "locally_built": True,
                "overview": "The iconic Australian doorless micro-sports roadster designed by Bill Buckle, featuring an ultra-light 345kg fiberglass body and rear-mounted Glas 2-stroke engine.",
                "generations": [
                    {
                        "series_code": "Dart",
                        "generation_name": "Goggomobil Dart",
                        "years": {"start": 1959, "end": 1962},
                        "body_styles": ["2-door-less open roadster"],
                        "summary": "Glas 293cc/392cc twin 2-stroke (11kW-15kW), 4-speed electric pre-selector gearbox, 345 kg curb weight; ~700 built in Sydney."
                    }
                ]
            },
            {
                "model_slug": "sedan-coupe-van",
                "name": "Buckle Goggomobil Sedan / Coupe / Van",
                "vehicle_type": "Microcar / Van",
                "segment": "Microcar",
                "years_sold_au": {"start": 1958, "end": 1961},
                "locally_built": True,
                "overview": "Locally molded fiberglass-bodied Goggomobil microcars produced in Sydney, including the Regent sedan, TS coupe, and Transporter van.",
                "generations": [
                    {
                        "series_code": "T-TS-TL",
                        "generation_name": "Buckle Goggomobil Range",
                        "years": {"start": 1958, "end": 1961},
                        "body_styles": ["2-door sedan (Regent)", "2-door coupe (TS)", "Panel van (Transporter)"],
                        "summary": "300cc and 400cc 2-stroke engines, suicide doors, full fiberglass construction made in Brookvale, NSW."
                    }
                ]
            }
        ]
    },
    "giocattolo": {
        "make_slug": "giocattolo",
        "name": "Giocattolo",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 1986, "end": 1989},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Giocattolo Motori Pty Ltd was established in 1986 in Caloundra, Queensland by automotive entrepreneur Paul Halstead and former McLaren Formula 1 engineer Barry Lock. Conceived as Australia's answer to the Ferrari 288 GTO and Porsche 959, the Giocattolo ('toy' in Italian) began with brand-new Alfa Romeo Sprint bodyshells imported from Italy. The front drivetrain was discarded, replaced by a mid-mounted Walkinshaw-fettled Holden Special Vehicles 5.0-litre Group A V8 (220kW/300hp) linked to a bespoke ZF 5-speed transaxle, Kevlar/carbon-fibre composite bodywork, and Brembo racing brakes. Capable of 0-100 km/h in 4.5 seconds and 260 km/h, the Giocattolo was an extraordinary Australian supercar feat. Only 15 production cars were completed before operations ceased in 1989.",
        "australian_history": "Paul Halstead, a wealthy computer entrepreneur who ran 'The Toy Shop' exotic car dealership in Sydney, dreamed of creating a bespoke mid-engine Australian sports car. Partnering with Barry Lock, formerly chief engineer at McLaren F1 and Can-Am racing, they established a factory at Caloundra on the Sunshine Coast of Queensland.\n\nHalstead initially intended to use the Alfa Romeo 2.5-litre Busso V6 mounted amidships behind the front seats. However, importing and tuning the Italian engines proved complex, expensive, and fragile. Halstead approached Tom Walkinshaw of Holden Special Vehicles (HSV). An agreement was reached for HSV to supply brand-new Holden 5.0-litre (5000i) fuel-injected V8s built to VL SS Group A Walkinshaw specifications. Halstead paired the thumping Australian V8 with an imported ZF 5DS-25/2 five-speed transaxle—the same gearbox used in the Ford GT40, De Tomaso Pantera, and BMW M1.\n\nLock redesigned the chassis from the bulkhead back, fabricating a rigid tubular rear spaceframe with double-wishbone independent suspension, cockpit-adjustable anti-roll bars, and four-piston Brembo disc brakes. Widebody Kevlar and carbon-fibre wheel arches gave the car an aggressive Group B rally stance. With 220 kW (300 bhp) pushing just 1,085 kg, the Giocattolo blasted from 0-100 km/h in 4.5 seconds and completed the standing quarter-mile in 12.8 seconds, comfortably out-accelerating contemporary Ferraris. However, escalating costs and the sudden withdrawal of promised Queensland State Government industrial development subsidies forced the company into liquidation in 1989. In total, only 3 Alfa V6 prototypes and 15 Holden V8 production cars were built.",
        "models_catalog": [
            {
                "model_slug": "group-b",
                "name": "Giocattolo Group B",
                "vehicle_type": "Coupe",
                "segment": "Supercar / Exotic",
                "years_sold_au": {"start": 1986, "end": 1989},
                "locally_built": True,
                "overview": "Australian mid-engine supercar combining modified Alfa Romeo Sprint bodywork with a mid-mounted 220kW Holden Group A 5.0L V8 and ZF transaxle.",
                "generations": [
                    {
                        "series_code": "Group-B",
                        "generation_name": "Giocattolo Group B V8",
                        "years": {"start": 1986, "end": 1989},
                        "body_styles": ["2-door mid-engine coupe"],
                        "summary": "Mid-mounted HSV/Holden 5.0L V8 (220kW/400Nm), ZF 5-speed transaxle, Kevlar panels, Brembo brakes, 0-100 in 4.5s; 15 production cars built."
                    }
                ]
            }
        ]
    },
    "oka": {
        "make_slug": "oka",
        "name": "OKA Motor Company",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 1986, "end": 2011},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "OKA Motor Company was established in 1986 in Bibra Lake, Perth, Western Australia to engineer and manufacture an uncompromising, severe-duty all-terrain four-wheel-drive commercial vehicle. Designed to conquer the harshest Australian outback conditions for mining companies, outback tour operators, and emergency services, the OKA featured a massive perimeter steel box-section chassis, heavy-duty Dana 60 front and Dana 70 rear live axles, a bulletproof New Process / Spicer transfer case, and Perkins 4-cylinder (Phaser 110MT) or Cummins 5.9L ISBe turbo-diesel engines. Available across LT, XT, and NT series in single-cab, dual-cab, multicab, bus, and van configurations, the OKA earned legendary status throughout the Kimberley, Pilbara, and Red Centre as an unyielding off-road machine capable of crossing rivers and sand dunes where standard 4WDs perished.",
        "australian_history": "The OKA story began in 1986 when a consortium of Western Australian mining, engineering, and transport executives sought a vehicle capable of transporting personnel and heavy cargo across remote unsealed washboard tracks, sand dunes, and boulder-strewn creek beds. Conventional commercial 4WDs (such as LandCruisers and Land Rovers) suffered chassis failures when heavily laden, while medium 4x4 trucks were too heavy and cumbersome. Engineering began at Bibra Lake, Perth, focused on extreme structural rigidity and serviceability in remote bush workshops.\n\nThe resulting chassis was constructed from heavy-gauge rectangular hollow-section steel, with full hot-dip galvanizing options. Heavy-duty Dana 60 front and Dana 70 rear rigid drive axles on long semi-elliptic leaf springs offered exceptional wheel articulation and ground clearance. The powertrain selected was the indestructible Perkins Phaser 110MT 4.0-litre four-cylinder turbo-diesel, mated to a Spicer 5-speed manual gearbox and New Process dual-range transfer case.\n\nOKA offered the platform in versatile body options: Single Cab chassis, Dual Cab, Multicab (seating up to 8), high-roof Commuter Bus (seating up to 14 tourists), and Panel Van. The cab styling was brutally functional, featuring flat glass panels that could be replaced easily in the Outback. OKAs quickly became standard equipment for Rio Tinto and BHP in the Pilbara, Telstra line maintenance in the Northern Territory, outback safari tours, and rural fire services. The XT series introduced mechanical refinements, and the NT series integrated Cummins 5.9-litre common-rail turbo-diesel engines. Around 500 OKAs were built before manufacturing ceased in 2011, remaining among Australia's most rugged and prized expedition vehicles.",
        "models_catalog": [
            {
                "model_slug": "4x4-truck",
                "name": "OKA 4x4 (LT, XT, NT)",
                "vehicle_type": "Cab Chassis / Van / Bus",
                "segment": "Heavy-Duty All-Terrain Commercial",
                "years_sold_au": {"start": 1986, "end": 2011},
                "locally_built": True,
                "overview": "Western Australian severe-duty 4WD truck and bus featuring box-section chassis, Dana axles, and Perkins/Cummins turbo-diesel power.",
                "generations": [
                    {
                        "series_code": "LT-XT-NT",
                        "generation_name": "OKA 4x4 Range (LT, XT, NT)",
                        "years": {"start": 1986, "end": 2011},
                        "body_styles": ["Single Cab", "Dual Cab", "Multicab", "Commuter Bus", "Van"],
                        "summary": "Perkins 4.0L Phaser turbo-diesel (82kW/353Nm) and Cummins 5.9L ISBe; Dana 60/70 axles, dual-range 4WD, 5.5-tonne GVM."
                    }
                ]
            }
        ]
    },
    "brabham": {
        "make_slug": "brabham",
        "name": "Brabham Automotive",
        "country_of_origin": "Australia",
        "years_active_au": {"start": 2018, "end": 2024},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Brabham Automotive was established in 2018 in Adelaide, South Australia by David Brabham (son of triple Formula One World Champion Sir Jack Brabham) in partnership with Australian advanced manufacturing company Fusion Capital. Operating from a state-of-the-art facility in Edinburgh Parks, Adelaide, Brabham set out to build an uncompromised track and road hypercar: the Brabham BT62. Weighing just 972 kg dry, the BT62 featured a carbon-fibre composite monocoque chassis, advanced aerodynamics generating over 1,200 kg of downforce, carbon-carbon brakes, and a mid-mounted naturally aspirated 5.4-litre modular V8 generating 522 kW (700 hp) and 667 Nm, revving to 8,200 rpm through a 6-speed Holinger sequential paddle-shift racing gearbox. In 2020, Brabham introduced the road-compliant BT62R. The vehicle achieved lap records at Mount Panorama and Adelaide Motorsport Festival before operations concluded in 2024.",
        "australian_history": "Sir Jack Brabham remains the only driver in Formula One history to win the World Championship in a car bearing his own name (1966). Decades later, his son David Brabham—himself an F1 driver and Le Mans 24 Hour winner—sought to resurrect the iconic Brabham marque as an Australian supercar manufacturer.\n\nForming a partnership with Adelaide investment firm Fusion Capital, Brabham Automotive established its engineering and assembly facility in Edinburgh Parks, northern Adelaide. The team engineered the BT62—the 62nd Brabham racing designator—as an uncompromised, purist track hypercar without turbochargers or hybrid batteries.\n\nAt its core was a lightweight high-tensile tubular steel chassis with integrated FIA safety cell and carbon-kevlar composite body panels, yielding a dry weight of just 972 kg. Aerodynamic development generated an astonishing 1,200 kg of downforce at 250 km/h. The powertrain was an Australian-tuned 5.4-litre quad-cam naturally aspirated V8 producing 522 kW (700 bhp) and 667 Nm, breathing through dry-sump lubrication and mated to an Australian-made Holinger six-speed sequential paddle-shift racing transmission. In February 2019, Luke Youlden shattered the Mount Panorama closed-cockpit lap record in a BT62 with a lap of 1m 58.69s.\n\nIn September 2020, Brabham launched the BT62R road-legal version, fitted with a front axle lift kit, air conditioning, heated windscreen, reversing camera, and road-compliant muffler and lighting. Brabham planned a 70-car production run celebrating Jack Brabham's 70-year racing legacy. However, the partnership between David Brabham and Fusion Capital concluded in early 2024, closing this brief but spectacular chapter in Australian hypercar engineering.",
        "models_catalog": [
            {
                "model_slug": "bt62",
                "name": "Brabham BT62 / BT62R",
                "vehicle_type": "Track / Road Hypercar",
                "segment": "Hypercar",
                "years_sold_au": {"start": 2018, "end": 2024},
                "locally_built": True,
                "overview": "Adelaide-built carbon-composite hypercar powered by a naturally aspirated 5.4L V8 (522kW/700hp), generating 1,200kg of downforce and setting lap records at Bathurst.",
                "generations": [
                    {
                        "series_code": "BT62",
                        "generation_name": "Brabham BT62 & BT62R",
                        "years": {"start": 2018, "end": 2024},
                        "body_styles": ["2-door track hypercar", "2-door road-compliant coupe (BT62R)"],
                        "summary": "5.4L quad-cam NA V8 (522kW/667Nm), 6-speed Holinger sequential, carbon-carbon brakes, 1,200 kg downforce, 972 kg dry weight."
                    }
                ]
            }
        ]
    }
}
