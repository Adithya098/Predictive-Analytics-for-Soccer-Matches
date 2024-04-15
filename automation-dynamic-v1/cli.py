from argparse import ArgumentParser, Namespace



def get_parser() -> ArgumentParser:
    parser = ArgumentParser()

    parser.add_argument("-s", "--sampling", action="store_true",
                        help="do sampling instead of whole execution to save time")

    parser.add_argument("-t", "--template", type=str, default="template.txt",
                        help="input template file name (default: %(default)s)")

    return parser

