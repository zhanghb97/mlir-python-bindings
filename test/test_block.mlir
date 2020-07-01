func @correct_number_of_regions() {
    // CHECK: test.two_region_op
    "test.two_region_op"()(
      {"work"() : () -> ()},
      {"work"() : () -> ()}
    ) : () -> ()
    return
}

func @extra_regions() {
    // expected-error@+1 {{expected 2 regions}}
    "test.two_region_op"()(
      {"work"() : () -> ()},
      {"work"() : () -> ()},
      {"work"() : () -> ()}
    ) : () -> ()
    return
}
