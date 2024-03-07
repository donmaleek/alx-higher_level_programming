def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    except Exception as e:
        print("An error occurred:", e)
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
