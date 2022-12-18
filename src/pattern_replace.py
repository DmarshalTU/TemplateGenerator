import os
import re
import logging
import glob
from pathlib import Path
import sh


logging.basicConfig(filename="app.log", filemode="w", level=logging.INFO)


def pattern_replace(proj_der: str, conf_dir: str) -> None:
    q = proj_der
    path = f"{proj_der}{conf_dir}"
    a = re.sub("[^A-Za-z]+", " ", proj_der).lower()
    b = a.replace(" ", "/")
    path = Path(f"{path}/{b}")
    path.mkdir(parents=True, exist_ok=True)

    for filename in glob.iglob(f"{proj_der}" + "**/**", recursive=True):
        if os.path.isfile(filename):
            a = re.sub("[^A-Za-z]+", " ", proj_der).title()
            b = "".join(e for e in a if e.isalnum())

            name_map = {"SingleSourceSpringKstreamPrototype": b}

            for root, _, files in os.walk(q):
                for f in files:
                    for name in name_map.keys():
                        if re.search(name, f) is not None:
                            new_name = re.sub(name, name_map[name], f)
                            try:
                                os.rename(
                                    os.path.join(root, f), os.path.join(root, new_name)
                                )
                            except OSError:
                                print("No such file or directory!")
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    s = f.read()
                    if "SingleSourceSpringKstreamPrototype" in s:
                        logging.info(f"Found in {filename}")
                        with open(filename, "w", encoding="utf-8") as f:
                            a = re.sub("[^A-Za-z]+", " ", q).title()
                            b = "".join(e for e in a if e.isalnum())
                            f.write(s.replace("SingleSourceSpringKstreamPrototype", b))

                            logging.info(f"Replaced in {filename}")

                with open(filename, "r", encoding="utf-8") as f:
                    s = f.read()
                    if "singleSourceSpringKstreamPrototype" in s:
                        logging.info(f"Found in {filename}")
                        with open(filename, "w", encoding="utf-8") as f:
                            a = re.sub("[^A-Za-z]+", " ", q).title()
                            b = "".join(e for e in a if e.isalnum())
                            c = b[0].lower() + b[1:]
                            f.write(s.replace("singleSourceSpringKstreamPrototype", c))
                            logging.info(f"Replaced in {filename}")

                with open(filename, "r", encoding="utf-8") as f:
                    s = f.read()
                    if "single.source.spring.kstream.prototype" in s:
                        logging.info(f"Found in {filename}")
                        with open(filename, "w", encoding="utf-8") as f:
                            a = re.sub("[^A-Za-z]+", " ", q).lower()
                            b = a.replace(" ", ".")
                            f.write(
                                s.replace("single.source.spring.kstream.prototype", b)
                            )
                            logging.info(f"Replaced in {filename}")

                with open(filename, "r", encoding="utf-8") as f:
                    s = f.read()
                    if "single-source-spring-kstream-prototype" in s:
                        logging.info(f"Found in {filename}")
                        with open(filename, "w", encoding="utf-8") as f:
                            a = re.sub("[^A-Za-z]+", " ", q).lower()
                            b = a.replace(" ", "-")
                            f.write(
                                s.replace("single-source-spring-kstream-prototype", b)
                            )
                            logging.info(f"Replaced in {filename}")

                with open(filename, "r", encoding="utf-8") as f:
                    s = f.read()
                    if "single/source/spring/kstream/prototype" in s:
                        logging.info(f"Found in {filename}")
                        with open(filename, "w", encoding="utf-8") as f:
                            a = re.sub("[^A-Za-z]+", " ", q).lower()
                            b = a.replace(" ", "/")
                            f.write(
                                s.replace("single/source/spring/kstream/prototype", b)
                            )
                            logging.info(f"Replaced in {filename}")

            except UnicodeDecodeError as e:
                logging.error(f"UnicodeDecodeError: {e}\nin {filename}")
                continue

    try:
        sh.cp(
            "-a",
            f"{proj_der}/src/main/java/io/cyren/ds/single/source/spring/kstream/prototype/",
            path,
        )
        sh.rm("-rf", f"{proj_der}/src/main/java/io/cyren/ds/single")
    except Exception as e:
        print(e)
