import lower as lw
import admin as ad


def run():
    name = input("Dame tu nombre: ")
    name = lw.lower(name)
    print(ad.checar_admin(name))
    



if __name__ == "__main__":
    run()