from controller.manager import Manager


def run():
    manager = Manager()
    manager.save_analyzed_data()


if __name__ == '__main__':
    run()