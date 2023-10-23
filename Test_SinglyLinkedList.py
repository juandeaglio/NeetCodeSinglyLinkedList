import unittest

from main import LinkedList


class MyTestCase(unittest.TestCase):
    def test_get_from_empty_linked_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.get(0), -1)

    def test_start_linked_list_and_remove_head(self):
        linked_list = LinkedList()
        linked_list.insertHead(1)
        self.assertEqual(1, linked_list.remove(0))

if __name__ == '__main__':
    unittest.main()
