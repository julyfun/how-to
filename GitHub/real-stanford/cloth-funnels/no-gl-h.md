---
title: no-gl-h
date: 2023-09-15 21:08:20
tags: ["GitHub", "real-stanford", "cloth-funnels"]
---
## Fault

```
In file included from /home/xuehan/Documents/GitHub/real-stanford/cloth-funnels/cloth_funnels/PyFlex/bindings/opengl/shader.cpp:28:
/home/xuehan/Documents/GitHub/real-stanford/cloth-funnels/cloth_funnels/PyFlex/bindings/opengl/shader.h:50:10: fatal error: GL/gl.h: No such file or directory
   50 | #include <GL/gl.h>
      |          ^~~~~~~~~
compilation terminated.
make[2]: *** [CMakeFiles/pyflex.dir/build.make:271: CMakeFiles/pyflex.dir/opengl/shader.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
In file included from /home/xuehan/Documents/GitHub/real-stanford/cloth-funnels/cloth_funnels/PyFlex/bindings/opengl/imguiRenderGL.cpp:25:
/home/xuehan/Documents/GitHub/real-stanford/cloth-funnels/cloth_funnels/PyFlex/bindings/opengl/shader.h:50:10: fatal error: GL/gl.h: No such file or directory
   50 | #include <GL/gl.h>
      |          ^~~~~~~~~
compilation terminated.
make[2]: *** [CMakeFiles/pyflex.dir/build.make:258: CMakeFiles/pyflex.dir/opengl/imguiRenderGL.cpp.o] Error 1
In file included from /home/xuehan/Documents/GitHub/real-stanford/cloth-funnels/cloth_funnels/PyFlex/bindings/opengl/../../external/glad/src/glad_egl.c:160,
                 from /home/xuehan/Documents/GitHub/real-stanford/cloth-funnels/cloth_funnels/PyFlex/bindings/opengl/shadersGL.cpp:39:
/home/xuehan/Documents/GitHub/real-stanford/cloth-funnels/cloth_funnels/PyFlex/bindings/opengl/../../external/glad/src/../include/glad/glad_egl.h:199:10: fatal error: EGL/eglplatform.h: No such file or directory
  199 | #include <EGL/eglplatform.h>
```

## Sol

```
sudo apt install freeglut3-dev
```

