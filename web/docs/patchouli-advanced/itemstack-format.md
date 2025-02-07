# ItemStack String Format

In multiple places in the book, you'll see values that can be filled with "ItemStack
Strings". An ItemStack String is simply a bit of text that can be read by the game to
create an instance of an item stack. This page outlines the format for them.

## Format 

Any of the following are allowed:

* **namespace:path** (e.g. `"minecraft:sword"`)
* **namespace:path#count** (e.g. `"minecraft:stone#64"`)
* **namespace:path{nbt}** (e.g. `"minecraft:diamond_pickaxe{display:{Lore:['A really cool
  pickaxe']}"`
* **namespace:path#count{nbt}**

To represent NBT tags with text inside, you can either replace all double quotes (`"`)
with single quotes (`'`), or escape them (`\"`). If you want to write a single quote,
you'll have to double-escape it (`\\'`).
