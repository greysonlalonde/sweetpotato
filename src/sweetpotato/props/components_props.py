"""
Provides props for components.
"""
BUTTON_PROPS = {
    "color",
    "hasTVPreferredFocus",
    "touchSoundDisabled",
    "title",
    "onPress",
    "children",
}

IMAGE_PROPS = {
    "onPartialLoad",
    "onProgress",
    "onLoadStart",
    "onLoadEnd",
    "onError",
    "onLoad",
    "resizeMethod",
    "loadingIndicatorSource",
    "style",
    "source",
    "blurRadius",
    "progressiveRenderingEnabled",
    "defaultSource",
    "fadeDuration",
    "capInsets",
    "resizeMode",
}

NAVIGATION_PROPS = {}

SCROLL_VIEW_PROPS = {
    "StickyHeaderComponent",
    "alwaysBounceHorizontal",
    "alwaysBounceVertical",
    "automaticallyAdjustContentInsets",
    "automaticallyAdjustsScrollIndicatorInsets",
    "bounces",
    "bouncesZoom",
    "canCancelContentTouches",
    "centerContent",
    "contentContainerStyle",
    "contentInset",
    "contentInsetAdjustmentBehavior",
    "contentOffset",
    "decelerationRate",
    "directionalLockEnabled",
    "disableIntervalMomentum",
    "disableScrollViewPanResponder",
    "fadingEdgeLength",
    "horizontal",
    "indicatorStyle",
    "invertStickyHeaders",
    "keyboardDismissMode",
    "keyboardShouldPersistTaps",
    "maintainVisibleContentPosition",
    "maximumZoomScale",
    "minimumZoomScale",
    "nestedScrollEnabled",
    "onContentSizeChange",
    "onMomentumScrollBegin",
    "onScroll",
    "onScrollBeginDrag",
    "onScrollEndDrag",
    "onScrollToTop",
    "overScrollMode",
    "pagingEnabled",
    "persistentScrollbar",
    "pinchGestureEnabled",
    "refreshControl",
    "removeClippedSubviews",
    "scrollEnabled",
    "scrollIndicatorInsets",
    "scrollPerfTag",
    "scrollToOverflowEnabled",
    "scrollsToTop",
    "showsHorizontalScrollIndicator",
    "showsVerticalScrollIndicator",
    "snapToAlignment",
    "snapToEnd",
    "snapToInterval",
    "snapToStart",
    "stickyHeaderHiddenOnScroll",
    "stickyHeaderIndices",
    "zoomScale",
    # "scrollEventThrottle",
    # "snapToOffsets",
    # "onMomentumScrollEnd",
    # "endFillColor",
    # "decelerationRate",
    # "scrollsToTop",
    # "disableIntervalMomentum",
    # "alwaysBounceVertical",
    # "snapToAlignment",
    # "maximumZoomScale",
    # "scrollPerfTag",
    # "showsVerticalScrollIndicator",
    # "keyboardShouldPersistTaps",
    # "centerContent",
    # "nestedScrollEnabled",
    # "snapToEnd",
    # "snapToStart",
    # "disableScrollViewPanResponder",
    # "keyboardDismissMode",
    # "automaticallyAdjustContentInsets",
    # "contentOffset",
    # "StickyHeaderComponent",
    # "canCancelContentTouches",
    # "pagingEnabled",
    # "onScrollBeginDrag",
    # "minimumZoomScale",
    # "overScrollMode",
    # "onMomentumScrollBegin",
    # "stickyHeaderHiddenOnScroll",
    # "stickyHeaderIndices",
    # "contentInset",
    # "snapToInterval",
    # "persistentScrollbar",
    # "onScrollEndDrag",
    # "refreshControl",
    # "invertStickyHeaders",
    # "scrollIndicatorInsets",
    # "bounces",
    # "contentInsetAdjustmentBehavior",
    # "showsHorizontalScrollIndicator",
    # "directionalLockEnabled",
    # "contentContainerStyle",
    # "fadingEdgeLength",
    # "maintainVisibleContentPosition",
    # "alwaysBounceHorizontal",
    # "horizontal",
    # "onScrollToTop",
    # "bouncesZoom",
    # "zoomScale",
    # "scrollToOverflowEnabled",
    # "indicatorStyle",
    # "pinchGestureEnabled",
    # "automaticallyAdjustsScrollIndicatorInsets",
}

FLAT_LIST_PROPS = {}

TEXT_PROPS = {
    "children",
    "accessibilityHint",
    "accessibilityLabel",
    "accessibilityRole",
    "accessibilityState",
    "accessibilityActions",
    "onAccessibilityAction",
    "accessible",
    "adjustsFontSizeToFit",
    "allowFontScaling",
    "android_hyphenationFrequency",
    "dataDetectorType",
    "disabled",
    "ellipsizeMode",
    "maxFontSizeMultiplier",
    "minimumFontScale",
    "nativeID",
    "numberOfLines",
    "onLayout",
    "onLongPress",
    "onMoveShouldSetResponder",
    "onPress",
    "onResponderGrant",
    "onResponderMove",
    "onResponderRelease",
    "onResponderTerminate",
    "onResponderTerminationRequest",
    "onStartShouldSetResponderCapture",
    "onTextLayout",
    "pressRetentionOffset",
    "selectable",
    "selectionColor",
    "suppressHighlighting",
    "textBreakStrategy",
    "style",
    "text"
    # "suppressHighlighting",
    # "ellipsizeMode",
    # "dataDetectorType",
    # "selectable",
    # "onTextLayout",
    # "android_hyphenationFrequency",
    # "adjustsFontSizeToFit",
    # "minimumFontScale",
    # "pressRetentionOffset",
    # "onLongPress",
}

TEXT_INPUT_PROPS = {
    "allowFontScaling",
    "autoCapitalize",
    "autoComplete",
    "autoCorrect",
    "autoFocus",
    "blurOnSubmit",
    "caretHidden",
    "clearButtonMode",
    "clearTextOnFocus",
    "contextMenuHidden",
    "dataDetectorTypes",
    "defaultValue",
    "disableFullscreenUI",
    "editable",
    "enablesReturnKeyAutomatically",
    "importantForAutofill",
    "inlineImageLeft",
    "inlineImagePadding",
    "inputAccessoryViewID",
    "keyboardAppearance",
    "keyboardType",
    "maxFontSizeMultiplier",
    "maxLength",
    "multiline",
    "numberOfLines",
    "onBlur",
    "onChange",
    "onChangeText",
    "onContentSizeChange",
    "onEndEditing",
    "onPressIn",
    "onPressOut",
    "onFocus",
    "onKeyPress",
    "onLayout",
    "onScroll",
    "onSelectionChange",
    "onSubmitEditing",
    "placeholder",
    "placeholderTextColor",
    "returnKeyLabel Android",
    "returnKeyType",
    "rejectResponderTermination",
    "scrollEnabled",
    "secureTextEntry",
    "selection",
    "selectionColor",
    "selectTextOnFocus",
    "showSoftInputOnFocus",
    "spellCheck",
    "textAlign",
    "textContentType",
    "passwordRules",
    "textBreakStrategy",
    "underlineColorAndroid",
    "value",
    # "onPressIn",
    # "secureTextEntry",
    # "returnKeyType",
    # "contextMenuHidden",
    # "placeholder",
    # "disableFullscreenUI",
    # "importantForAutofill",
    # "maxLength",
    # "spellCheck",
    # "editable",
    # "multiline",
    # "showSoftInputOnFocus",
    # "caretHidden",
    # "onEndEditing",
    # "onChange",
    # "textAlign",
    # "onSelectionChange",
    # "onSubmitEditing",
    # "defaultValue",
    # "onFocus",
    # "selection",
    # "autoCapitalize",
    # "rejectResponderTermination",
    # "keyboardType",
    # "autoFocus",
    # "onKeyPress",
    # "placeholderTextColor",
    # "returnKeyLabel Android",
    # "value",
    # "keyboardAppearance",
    # "onPressOut",
    # "enablesReturnKeyAutomatically",
    # "underlineColorAndroid",
    # "selectTextOnFocus",
    # "clearTextOnFocus",
    # "textContentType",
    # "passwordRules",
    # "inlineImagePadding",
    # "inlineImageLeft",
    # "blurOnSubmit",
    # "autoComplete",
    # "autoCorrect",
    # "clearButtonMode",
    # "dataDetectorTypes",
    # "onBlur",
    # "inputAccessoryViewID",
    # "onChangeText",
    "secureTextEntry",
}

INPUT_PROPS = {"onChangeText", "placeholder", "value", "secureTextEntry"}

VIEW_PROPS = {
    "accessibilityActions",
    "accessibilityElementsHidden",
    "accessibilityHint",
    "accessibilityIgnoresInvertColors",
    "accessibilityLabel",
    "accessibilityLiveRegion",
    "accessibilityRole",
    "accessibilityState",
    "accessibilityValue",
    "accessibilityViewIsModal",
    "accessible",
    "collapsable",
    "focusable",
    "hitSlop",
    "importantForAccessibility",
    "nativeID",
    "needsOffscreenAlphaCompositing",
    "nextFocusDown",
    "nextFocusForward",
    "nextFocusLeft",
    "nextFocusRight",
    "nextFocusUp",
    "onAccessibilityAction",
    "onAccessibilityEscape",
    "onAccessibilityTap",
    "onLayout",
    "onMagicTap",
    "onMoveShouldSetResponder",
    "onMoveShouldSetResponderCapture",
    "onResponderGrant",
    "onResponderMove",
    "onResponderReject",
    "onResponderRelease",
    "onResponderTerminate",
    "onResponderTerminationRequest",
    "onStartShouldSetResponder",
    "onStartShouldSetResponderCapture",
    "pointerEvents",
    "removeClippedSubviews",
    "renderToHardwareTextureAndroid",
    "shouldRasterizeIOS",
    "style",
    # "importantForAccessibility",
    # "hitSlop",
    # "focusable",
    # "collapsable",
    # "accessibilityElementsHidden",
    # "onAccessibilityTap",
    # "onStartShouldSetResponder",
    # "onMoveShouldSetResponderCapture",
    # "onResponderReject",
    # "pointerEvents",
    # "renderToHardwareTextureAndroid",
    # "shouldRasterizeIOS",
    # "accessibilityLiveRegion",
    # "accessibilityViewIsModal",
    # "needsOffscreenAlphaCompositing",
    # "accessibilityValue",
    # "accessibilityIgnoresInvertColors",
    # "onAccessibilityEscape",
    # "onMagicTap",
    "children",
}

ACTIVITY_INDICATOR_PROPS = {
    # need to look at extending view props here
    "animating",
    "color",
    "hidesWhenStopped",
    "size",
}

TOUCHABLE_OPACITY_PROPS = {}

STYLE_SHEET_PROPS = {}

APP_PROPS = {"state"}

SAFE_AREA_PROVIDER_PROPS = {
    "children",
}
