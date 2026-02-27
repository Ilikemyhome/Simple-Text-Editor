import unittest
from TextEditor import TextEditor


class TestTextEditor(unittest.TestCase):
    def test_1_addOne(self):
        editor = TextEditor()
        editor.add_char("a")
        self.assertEqual(editor.text, "a")

    def test_2_addMultiple(self):
        editor = TextEditor()
        editor.add_char("h")
        editor.add_char("i")

        self.assertEqual(editor.text, "hi")

    def test_3_UndoAdd(self):
        editor = TextEditor()
        editor.add_char("h")
        editor.add_char("i")
        editor.undo()

        self.assertEqual(editor.text, "h")
    
    def test_4_UndoDelete(self):
        editor = TextEditor()
        editor.add_char("h")
        editor.add_char("i")
        editor.delete()
        editor.undo()

        self.assertEqual(editor.text, "hi")
    
    def test_5_delete(self):
        editor = TextEditor()
        editor.add_char("h")
        editor.add_char("i")
        editor.add_char("!")
        editor.delete()

        self.assertEqual(editor.text, "hi")


## edge Cases

    def test_6_DeleteEmpty(self):
        editor = TextEditor()
        editor.delete()

        self.assertEqual(editor.text, "")

    def test_7_EmptyUndo(self):
       
        editor = TextEditor()
        editor.undo()

        self.assertEqual(editor.text, "")

    def test_8_LongWord(self):
        editor = TextEditor()
        editor.add_char("t")
        editor.add_char("o")
        editor.add_char("g")
        editor.add_char("e")
        editor.add_char("t")
        editor.add_char("h")
        editor.add_char("e")
        editor.add_char("r")
        editor.delete()

        self.assertEqual(editor.text, "togethe")
    

    def test_9_MultipleUndo(self):
        editor = TextEditor()
        editor.add_char("t")
        editor.add_char("o")
        editor.add_char("g")
        editor.undo()
        editor.undo()
        editor.undo()
        editor.undo()

        editor.delete()

        self.assertEqual(editor.text, "")
    
if __name__== "__main__":
    unittest.main()
