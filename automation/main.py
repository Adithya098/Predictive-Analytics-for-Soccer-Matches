from pat import execute_pat, read_output_file, delete_output_file, parse_output
from crawl import send_request, find_teams, find_attributes

def main():
    # execute_pat()
    # output = read_output_file()
    # delete_output_file()
    # parse_output(output)
    soup = send_request("https://www.premierleague.com/match/12301")
    print(find_teams(soup))
    
    soup = send_request("https://sofifa.com/player/243245/orkun-kokcu/240032/?attr=classic")
    print(find_attributes(soup))
    #print(soup)
    
if __name__ == "__main__":
    main()