---
title: default-parameters
date: 2024-03-27 17:46:12
tags: ["langs", "rust"]
---
ref: https://www.thecodedmessage.com/posts/default-params/

## Sol 1

```rs
impl Default for WindowConfig {
    fn default() -> Self {
        Self {
            width: 100,
            height: 100,
            visibility: WindowVisibility::Visible,
            window_style: WindowStyle::Standard,
            z_position: -1,
            autoclose: AutoclosePolicy::Disable,
        }
    }
}

let handle = create_window(WindowConfig {
    width: 500,
    z_position: 2,
    autoclose: AutoclosePolicy::Enable,
    ..Default::default()
});
```

## Sol 2..

```rs
impl WindowBuilder {
    fn height(mut self, height: u32) -> Self {
        self.height = height;
        self
    }

    // ...
}

impl WindowBuilder {
    fn height(self, height: u32) -> Self {
        Self {
            height,
            ..self
        }
    }

    // ...
}

impl WindowBuilder {
    fn autoclose_enable(mut self) -> Self {
        self.autoclose = AutoclosePolicy::Enable;
        self
    }

    fn autoclose_disable(mut self) -> Self {
        self.autoclose = AutoclosePolicy::Disable;
        self
    }
}

impl WindowBuilder {
    fn build(self) {
        window_create(self)
    }
}


let handle = WindowBuilder::new()
    .width(500)
    .z_position(2)
    .autoclose_enable()
    .build();
```

