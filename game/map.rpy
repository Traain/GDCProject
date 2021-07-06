screen map:
    viewport:
        xalign 0.5 ypos 50 xysize (1280, 720)
        child_size (3200, 3200)

        draggable True
        mousewheel True
        arrowkeys True

        add "MAP.png"
        style_group "invstyle"
        frame:
            xpos 50 ypos 50
            button:
                text " Close " style "button_text"
                action Hide("map")
