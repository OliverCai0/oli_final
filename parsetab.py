
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONSTANTS DISPLAY DOUBLE FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE MESH MOVE POP PUSH ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SPHERE STRING TEXTURE TORUS TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEcommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,26,32,34,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[-1,0,-1,-3,-9,-10,-12,-14,-52,-61,-2,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'COMMENT':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[3,3,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'POP':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[4,4,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'PUSH':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[5,5,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SCREEN':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[6,6,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SAVE':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[7,7,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'DISPLAY':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[8,8,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SPHERE':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[9,9,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'TORUS':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[10,10,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'BOX':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[11,11,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'LINE':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[12,12,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'MOVE':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[13,13,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SCALE':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[14,14,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'ROTATE':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[15,15,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'FRAMES':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[16,16,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'BASENAME':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[17,17,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'VARY':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[18,18,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SET':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[19,19,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SET_KNOBS':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[20,20,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'AMBIENT':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[21,21,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'CONSTANTS':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[22,22,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'LIGHT':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[23,23,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SHADING':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[24,24,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'CAMERA':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[25,25,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'GENERATE_RAYFILES':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[26,26,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'MESH':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[27,27,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SAVE_KNOBS':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[28,28,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SAVE_COORDS':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[29,29,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'TWEEN':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[30,30,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'FOCAL':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[31,31,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'WEB':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[32,32,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'TEXTURE':([0,2,3,4,5,6,8,26,32,36,38,39,40,41,53,54,57,61,65,66,68,70,71,82,84,89,101,102,103,105,109,110,113,122,123,128,129,131,132,133,146,147,148,149,151,155,158,160,161,162,163,164,166,168,170,171,172,173,176,179,185,186,],[33,33,-3,-9,-10,-12,-14,-52,-61,-8,-6,-7,-4,-5,-41,-42,-45,-50,-57,-58,-60,-11,-13,-40,-44,-53,-36,-38,-39,-46,-55,-54,-15,-35,-37,-56,-59,-17,-16,-19,-18,-20,-21,-23,-27,-43,-51,-22,-24,-25,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'DOUBLE':([6,9,10,11,12,13,14,16,20,21,25,30,31,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,58,59,60,62,67,69,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,92,93,94,95,96,97,98,99,100,104,106,107,108,112,114,115,116,117,118,119,120,121,124,125,126,127,130,134,135,136,137,138,139,140,142,143,144,145,150,152,153,154,156,157,159,165,167,169,174,175,177,178,179,180,181,182,183,184,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,-8,-4,-5,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'STRING':([7,17,37,38,39,40,41,63,90,],[39,39,39,-6,-7,-4,-5,39,39,]),'XYZ':([7,9,10,11,12,15,17,18,19,22,23,27,28,29,33,36,37,38,39,40,41,63,82,89,90,91,99,101,102,110,111,113,121,132,133,141,148,149,151,162,164,166,172,],[40,40,40,40,40,52,40,40,40,40,40,40,40,40,40,-8,40,-6,-7,-4,-5,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'ID':([7,9,10,11,12,17,18,19,22,23,27,28,29,33,36,37,38,39,40,41,63,82,89,90,91,99,101,102,110,111,113,121,132,133,141,148,149,151,162,164,166,172,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,-8,41,-6,-7,-4,-5,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'SHADING_TYPE':([24,],[61,]),'CO':([27,40,41,64,],[63,-4,-5,90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,2,],[1,34,]),'command':([0,2,],[2,2,]),'NUMBER':([6,9,10,11,12,13,14,16,20,21,25,30,31,35,42,43,44,45,46,47,48,49,50,51,52,55,56,58,59,60,62,67,69,72,73,74,75,76,77,78,79,80,81,83,85,86,87,88,92,93,94,95,96,97,98,99,100,104,106,107,108,112,114,115,116,117,118,119,120,121,124,125,126,127,130,134,135,136,137,138,139,140,142,143,144,145,150,152,153,154,156,157,159,165,167,169,174,175,177,178,179,180,181,182,183,184,],[35,42,44,46,48,50,51,53,57,58,62,67,68,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,107,108,112,113,114,115,116,117,118,119,121,124,125,126,127,130,132,133,134,135,136,137,138,140,141,142,143,144,145,148,149,150,151,152,153,154,156,157,158,159,162,164,165,166,167,168,169,172,174,175,177,178,179,180,181,182,183,184,185,186,]),'TEXT':([7,17,37,63,90,],[37,54,71,89,110,]),'SYMBOL':([7,9,10,11,12,17,18,19,22,23,27,28,29,33,37,63,82,89,90,91,99,101,102,110,111,113,121,132,133,141,148,149,151,162,164,166,172,],[38,43,45,47,49,38,55,56,59,60,64,65,66,69,38,38,103,109,38,111,120,122,123,128,129,131,139,146,147,155,160,161,163,170,171,173,176,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',123),
  ('input -> command input','input',2,'p_input','mdl.py',124),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',128),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',132),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',133),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',137),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',138),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',142),
  ('command -> POP','command',1,'p_command_stack','mdl.py',146),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',147),
  ('command -> SCREEN NUMBER NUMBER','command',3,'p_command_screen','mdl.py',151),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',152),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',159),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',163),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',167),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',168),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',169),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',170),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',184),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',185),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',186),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',187),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',201),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',202),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',203),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',204),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',218),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',219),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',220),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',221),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',222),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',223),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',224),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',225),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',246),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',247),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',255),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',256),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',264),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',265),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',273),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',278),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_vary','mdl.py',283),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',292),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',293),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',304),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',310),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',311),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',317),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',323),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',329),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',334),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',338),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',339),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',340),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',341),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',355),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',361),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',368),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',373),
  ('command -> WEB','command',1,'p_web','mdl.py',377),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',381),
]
