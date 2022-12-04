
buffer_1 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x9f, 0xff, 0xff, 0xfe, 0x1f, 0xff, 
0xff, 0xf8, 0x1f, 0xff, 0xff, 0xe0, 0x1f, 0xff, 0xff, 0x80, 0x1f, 0xff, 0xff, 0x78, 0x1f, 0xff, 
0xff, 0xf8, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 
0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xf8, 0x1f, 0xff, 
0xff, 0xf0, 0x07, 0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_2 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x3f, 0xff, 0xff, 0x80, 0x07, 0xff, 
0xff, 0x00, 0x03, 0xff, 0xfc, 0x00, 0x01, 0xff, 0xfc, 0x00, 0x00, 0xff, 0xf8, 0x7f, 0x80, 0x7f, 
0xf1, 0xff, 0xc0, 0x7f, 0xf3, 0xff, 0xe0, 0x3f, 0xf7, 0xff, 0xf0, 0x3f, 0xe7, 0xff, 0xf8, 0x3f, 
0xef, 0xff, 0xf8, 0x3f, 0xef, 0xff, 0xf8, 0x3f, 0xff, 0xff, 0xf8, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 
0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xf8, 0x3f, 0xff, 0xff, 0xf8, 0x7f, 
0xff, 0xff, 0xf8, 0x7f, 0xff, 0xff, 0xf8, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xf1, 0xff, 
0xff, 0xff, 0xe3, 0xff, 0xff, 0xff, 0xe3, 0xff, 0xff, 0xff, 0xc7, 0xff, 0xff, 0xff, 0xcf, 0xff, 
0xff, 0xff, 0x9f, 0xff, 0xff, 0xff, 0x1f, 0xff, 0xff, 0xfe, 0x3f, 0xff, 0xff, 0xfe, 0x7f, 0xff, 
0xff, 0xfc, 0xff, 0xff, 0xff, 0xf9, 0xff, 0xff, 0xff, 0xf3, 0xff, 0xff, 0xff, 0xe7, 0xff, 0xff, 
0xff, 0xcf, 0xff, 0xff, 0xff, 0x9f, 0xff, 0xff, 0xff, 0x3f, 0xff, 0xf7, 0xfe, 0x3f, 0xff, 0xe7, 
0xfc, 0x7f, 0xff, 0xcf, 0xf8, 0x00, 0x00, 0x0f, 0xf0, 0x00, 0x00, 0x1f, 0xe0, 0x00, 0x00, 0x1f, 
0xc0, 0x00, 0x00, 0x1f, 0xc0, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_3 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x3f, 0xff, 0xff, 0x80, 0x0f, 0xff, 
0xff, 0x00, 0x07, 0xff, 0xfe, 0x00, 0x03, 0xff, 0xfc, 0x3e, 0x01, 0xff, 0xf8, 0xff, 0x80, 0xff, 
0xfb, 0xff, 0xc0, 0xff, 0xf7, 0xff, 0xe0, 0xff, 0xf7, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 
0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xe1, 0xff, 
0xff, 0xff, 0xe3, 0xff, 0xff, 0xff, 0xe3, 0xff, 0xff, 0xff, 0xc7, 0xff, 0xff, 0xff, 0xcf, 0xff, 
0xff, 0xff, 0x9f, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xff, 0xfc, 0x03, 0xff, 0xff, 0xf0, 0x01, 0xff, 
0xff, 0xc0, 0x00, 0xff, 0xff, 0xfc, 0x00, 0x7f, 0xff, 0xff, 0x80, 0x7f, 0xff, 0xff, 0xc0, 0x3f, 
0xff, 0xff, 0xf0, 0x3f, 0xff, 0xff, 0xf0, 0x3f, 0xff, 0xff, 0xf8, 0x3f, 0xff, 0xff, 0xf8, 0x3f, 
0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 
0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x7f, 0xff, 0xff, 0xf8, 0x7f, 
0xff, 0xff, 0xf8, 0xff, 0xfb, 0xff, 0xf1, 0xff, 0xe0, 0xff, 0xe3, 0xff, 0xe0, 0x3f, 0xc7, 0xff, 
0xe0, 0x00, 0x0f, 0xff, 0xf0, 0x00, 0x3f, 0xff, 0xfc, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_4 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 0xff, 0xff, 0xff, 0xf0, 0xff, 
0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xc0, 0xff, 0xff, 0xff, 0xc0, 0xff, 0xff, 0xff, 0x80, 0xff, 
0xff, 0xff, 0x00, 0xff, 0xff, 0xff, 0x20, 0xff, 0xff, 0xfe, 0x60, 0xff, 0xff, 0xfc, 0x60, 0xff, 
0xff, 0xfc, 0xe0, 0xff, 0xff, 0xf9, 0xe0, 0xff, 0xff, 0xf1, 0xe0, 0xff, 0xff, 0xf3, 0xe0, 0xff, 
0xff, 0xe7, 0xe0, 0xff, 0xff, 0xc7, 0xe0, 0xff, 0xff, 0x8f, 0xe0, 0xff, 0xff, 0x9f, 0xe0, 0xff, 
0xff, 0x3f, 0xe0, 0xff, 0xfe, 0x3f, 0xe0, 0xff, 0xfe, 0x7f, 0xe0, 0xff, 0xfc, 0xff, 0xe0, 0xff, 
0xf8, 0xff, 0xe0, 0xff, 0xf9, 0xff, 0xe0, 0xff, 0xf3, 0xff, 0xe0, 0xff, 0xe3, 0xff, 0xe0, 0xff, 
0xe7, 0xff, 0xe0, 0xff, 0xcf, 0xff, 0xe0, 0xff, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 
0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 
0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 
0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 
0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_5 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 0x00, 0x1f, 
0xff, 0xf0, 0x00, 0x1f, 0xff, 0xf0, 0x00, 0x3f, 0xff, 0xe0, 0x00, 0x3f, 0xff, 0xe0, 0x00, 0x3f, 
0xff, 0xcf, 0xff, 0xff, 0xff, 0xcf, 0xff, 0xff, 0xff, 0x9f, 0xff, 0xff, 0xff, 0x9f, 0xff, 0xff, 
0xff, 0x3f, 0xff, 0xff, 0xff, 0x3f, 0xff, 0xff, 0xfe, 0x0f, 0xff, 0xff, 0xfe, 0x01, 0xff, 0xff, 
0xfc, 0x00, 0x7f, 0xff, 0xfc, 0x00, 0x1f, 0xff, 0xf8, 0x00, 0x07, 0xff, 0xff, 0x00, 0x03, 0xff, 
0xff, 0xf8, 0x01, 0xff, 0xff, 0xfe, 0x00, 0xff, 0xff, 0xff, 0x80, 0xff, 0xff, 0xff, 0xc0, 0x7f, 
0xff, 0xff, 0xe0, 0x3f, 0xff, 0xff, 0xf0, 0x3f, 0xff, 0xff, 0xf8, 0x3f, 0xff, 0xff, 0xf8, 0x1f, 
0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xfe, 0x1f, 0xff, 0xff, 0xfe, 0x1f, 
0xff, 0xff, 0xfe, 0x1f, 0xff, 0xff, 0xfe, 0x1f, 0xff, 0xff, 0xfe, 0x3f, 0xff, 0xff, 0xfe, 0x3f, 
0xff, 0xff, 0xfe, 0x3f, 0xff, 0xff, 0xfe, 0x7f, 0xff, 0xff, 0xfc, 0x7f, 0xff, 0xff, 0xfc, 0xff, 
0xff, 0xff, 0xf9, 0xff, 0xf0, 0xff, 0xf3, 0xff, 0xe0, 0x7f, 0xe3, 0xff, 0xe0, 0x1f, 0x8f, 0xff, 
0xf0, 0x00, 0x1f, 0xff, 0xf8, 0x00, 0x7f, 0xff, 0xfe, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_6 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x0f, 0xff, 0xff, 0xf0, 0x3f, 
0xff, 0xff, 0xc3, 0xff, 0xff, 0xff, 0x07, 0xff, 0xff, 0xfe, 0x1f, 0xff, 0xff, 0xf8, 0x3f, 0xff, 
0xff, 0xf0, 0x7f, 0xff, 0xff, 0xe0, 0xff, 0xff, 0xff, 0xc1, 0xff, 0xff, 0xff, 0x83, 0xff, 0xff, 
0xff, 0x83, 0xff, 0xff, 0xff, 0x07, 0xff, 0xff, 0xfe, 0x0f, 0xff, 0xff, 0xfe, 0x0f, 0xff, 0xff, 
0xfc, 0x1f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xf8, 0x1f, 0xff, 0xff, 0xf8, 0x3f, 0x07, 0xff, 
0xf0, 0x38, 0x00, 0xff, 0xf0, 0x20, 0x00, 0x7f, 0xf0, 0x0f, 0xe0, 0x3f, 0xf0, 0x1f, 0xf0, 0x1f, 
0xe0, 0x7f, 0xf8, 0x0f, 0xe0, 0x7f, 0xfc, 0x0f, 0xe0, 0x7f, 0xfc, 0x07, 0xe0, 0x7f, 0xfe, 0x07, 
0xe0, 0x7f, 0xfe, 0x07, 0xe0, 0x7f, 0xfe, 0x07, 0xe0, 0xff, 0xff, 0x07, 0xe0, 0xff, 0xff, 0x07, 
0xe0, 0x7f, 0xff, 0x07, 0xe0, 0x7f, 0xff, 0x07, 0xe0, 0x7f, 0xff, 0x07, 0xf0, 0x7f, 0xff, 0x07, 
0xf0, 0x7f, 0xff, 0x07, 0xf0, 0x7f, 0xff, 0x0f, 0xf8, 0x3f, 0xff, 0x0f, 0xf8, 0x3f, 0xff, 0x1f, 
0xfc, 0x1f, 0xfe, 0x1f, 0xfe, 0x1f, 0xfe, 0x3f, 0xfe, 0x0f, 0xfc, 0x7f, 0xff, 0x07, 0xf8, 0xff, 
0xff, 0x83, 0xf1, 0xff, 0xff, 0xe0, 0x03, 0xff, 0xff, 0xf8, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_7 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x00, 0x00, 0x07, 
0xfc, 0x00, 0x00, 0x07, 0xfc, 0x00, 0x00, 0x07, 0xf8, 0x00, 0x00, 0x0f, 0xf8, 0x00, 0x00, 0x0f, 
0xf8, 0xff, 0xff, 0x0f, 0xf3, 0xff, 0xff, 0x1f, 0xf7, 0xff, 0xff, 0x1f, 0xe7, 0xff, 0xfe, 0x1f, 
0xef, 0xff, 0xfe, 0x3f, 0xff, 0xff, 0xfe, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x7f, 
0xff, 0xff, 0xfc, 0x7f, 0xff, 0xff, 0xf8, 0x7f, 0xff, 0xff, 0xf8, 0xff, 0xff, 0xff, 0xf8, 0xff, 
0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xf1, 0xff, 0xff, 0xff, 0xf1, 0xff, 0xff, 0xff, 0xe1, 0xff, 
0xff, 0xff, 0xe3, 0xff, 0xff, 0xff, 0xe3, 0xff, 0xff, 0xff, 0xc3, 0xff, 0xff, 0xff, 0xc7, 0xff, 
0xff, 0xff, 0xc7, 0xff, 0xff, 0xff, 0x87, 0xff, 0xff, 0xff, 0x8f, 0xff, 0xff, 0xff, 0x8f, 0xff, 
0xff, 0xff, 0x0f, 0xff, 0xff, 0xff, 0x1f, 0xff, 0xff, 0xff, 0x1f, 0xff, 0xff, 0xfe, 0x1f, 0xff, 
0xff, 0xfe, 0x3f, 0xff, 0xff, 0xfe, 0x3f, 0xff, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xfc, 0x7f, 0xff, 
0xff, 0xfc, 0x7f, 0xff, 0xff, 0xfc, 0x7f, 0xff, 0xff, 0xf8, 0xff, 0xff, 0xff, 0xf8, 0xff, 0xff, 
0xff, 0xf8, 0xff, 0xff, 0xff, 0xf1, 0xff, 0xff, 0xff, 0xf1, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_8 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 0x1f, 0xff, 0xff, 0xc0, 0x03, 0xff, 
0xff, 0x0f, 0xf0, 0xff, 0xfe, 0x1f, 0xf8, 0x7f, 0xfc, 0x3f, 0xfc, 0x3f, 0xfc, 0x7f, 0xfc, 0x3f, 
0xf8, 0x7f, 0xfe, 0x1f, 0xf8, 0x7f, 0xfe, 0x1f, 0xf8, 0x7f, 0xfe, 0x1f, 0xf8, 0x7f, 0xfe, 0x1f, 
0xf8, 0x7f, 0xfe, 0x1f, 0xf8, 0x3f, 0xfe, 0x1f, 0xf8, 0x3f, 0xfe, 0x1f, 0xf8, 0x1f, 0xfc, 0x3f, 
0xf8, 0x0f, 0xfc, 0x7f, 0xfc, 0x07, 0xf8, 0xff, 0xfe, 0x03, 0xf1, 0xff, 0xfe, 0x01, 0xe3, 0xff, 
0xff, 0x00, 0xc7, 0xff, 0xff, 0x80, 0x0f, 0xff, 0xff, 0xc0, 0x1f, 0xff, 0xff, 0xe0, 0x0f, 0xff, 
0xff, 0xf0, 0x07, 0xff, 0xff, 0xe0, 0x03, 0xff, 0xff, 0xc6, 0x01, 0xff, 0xff, 0x8f, 0x00, 0xff, 
0xff, 0x1f, 0x80, 0x7f, 0xfe, 0x3f, 0xc0, 0x3f, 0xfc, 0x3f, 0xe0, 0x1f, 0xf8, 0x7f, 0xf0, 0x1f, 
0xf8, 0x7f, 0xf8, 0x0f, 0xf8, 0x7f, 0xfc, 0x0f, 0xf0, 0x7f, 0xfe, 0x0f, 0xf0, 0xff, 0xfe, 0x0f, 
0xf0, 0xff, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0x0f, 0xf0, 0x7f, 0xff, 0x0f, 0xf8, 0x7f, 0xff, 0x0f, 
0xf8, 0x7f, 0xff, 0x1f, 0xfc, 0x3f, 0xfe, 0x1f, 0xfc, 0x3f, 0xfe, 0x3f, 0xfe, 0x1f, 0xfc, 0x7f, 
0xff, 0x07, 0xf8, 0xff, 0xff, 0xc1, 0xc3, 0xff, 0xff, 0xf8, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""

buffer_9 = """0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 0x1f, 0xff, 0xff, 0xc0, 0x07, 0xff, 
0xff, 0x8f, 0xc1, 0xff, 0xfe, 0x1f, 0xe0, 0xff, 0xfe, 0x3f, 0xf0, 0x7f, 0xfc, 0x7f, 0xf8, 0x7f, 
0xf8, 0x7f, 0xf8, 0x3f, 0xf8, 0xff, 0xfc, 0x1f, 0xf0, 0xff, 0xfc, 0x1f, 0xf0, 0xff, 0xfe, 0x0f, 
0xe0, 0xff, 0xfe, 0x0f, 0xe0, 0xff, 0xfe, 0x0f, 0xe0, 0xff, 0xfe, 0x0f, 0xe0, 0xff, 0xfe, 0x07, 
0xe0, 0xff, 0xfe, 0x07, 0xe0, 0xff, 0xff, 0x07, 0xe0, 0xff, 0xff, 0x07, 0xe0, 0xff, 0xfe, 0x07, 
0xe0, 0x7f, 0xfe, 0x07, 0xe0, 0x7f, 0xfe, 0x07, 0xf0, 0x3f, 0xfe, 0x07, 0xf0, 0x3f, 0xfe, 0x07, 
0xf0, 0x1f, 0xfe, 0x07, 0xf8, 0x0f, 0xfc, 0x07, 0xfc, 0x07, 0xf0, 0x0f, 0xfe, 0x00, 0x04, 0x0f, 
0xff, 0x00, 0x1c, 0x0f, 0xff, 0xe0, 0xfc, 0x1f, 0xff, 0xff, 0xf8, 0x1f, 0xff, 0xff, 0xf8, 0x1f, 
0xff, 0xff, 0xf8, 0x3f, 0xff, 0xff, 0xf0, 0x7f, 0xff, 0xff, 0xf0, 0x7f, 0xff, 0xff, 0xe0, 0xff, 
0xff, 0xff, 0xc1, 0xff, 0xff, 0xff, 0xc1, 0xff, 0xff, 0xff, 0x83, 0xff, 0xff, 0xff, 0x07, 0xff, 
0xff, 0xfe, 0x0f, 0xff, 0xff, 0xfc, 0x1f, 0xff, 0xff, 0xf8, 0x7f, 0xff, 0xff, 0xf0, 0xff, 0xff, 
0xff, 0xc3, 0xff, 0xff, 0xfe, 0x0f, 0xff, 0xff, 0xf0, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff"""


def convertion_to_py_bytearray(byte_arrays):
    answer = []
    help_array = byte_arrays.split(", ")
    for element in help_array:
        if element == ", ":
            help_array.remove(element)
    for element in help_array:
        if len(element) == 4:
            answer.append(element[1::])
        else:
            answer.append(element[2::])
    if len(answer) != 256:
        print("Something might have gone wrong...")
    return "\\" + "\\".join(answer)

buffer_1_py = convertion_to_py_bytearray(buffer_1) 
buffer_2_py = convertion_to_py_bytearray(buffer_2) 
buffer_3_py = convertion_to_py_bytearray(buffer_3) 
buffer_4_py = convertion_to_py_bytearray(buffer_4) 
buffer_5_py = convertion_to_py_bytearray(buffer_5) 
buffer_6_py = convertion_to_py_bytearray(buffer_6) 
buffer_7_py = convertion_to_py_bytearray(buffer_7) 
buffer_8_py = convertion_to_py_bytearray(buffer_8) 
buffer_9_py = convertion_to_py_bytearray(buffer_9)
