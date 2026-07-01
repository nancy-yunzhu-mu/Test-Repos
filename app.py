from corkage.lookup import get_corkage_info

def main():
    for r in get_corkage_info():
        print(f"{r['name']}: {r['corkage']}")

if __name__ == "__main__":
    main()
