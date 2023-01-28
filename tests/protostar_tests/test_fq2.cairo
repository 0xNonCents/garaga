%lang starknet

from src.pair import get_e_G1G2
from src.fq2 import FQ2, fq2 as fq2_lib
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.cairo_builtins import BitwiseBuiltin
from starkware.cairo.common.alloc import alloc

from starkware.cairo.common.uint256 import Uint256

@external
func __setup__() {
    %{
        from tools.py.utils import print_u_256_info
    %}
    assert 1 = 1;
    return ();
}



@external
func test_fq2_mul{
    syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr, bitwise_ptr: BitwiseBuiltin*
}() {
    alloc_locals;
    __setup__();
    local py_res_e0_low : felt;
    local py_res_e0_high : felt;
    local py_res_e1_low : felt;
    local py_res_e1_high : felt;

    local input : felt;

    %{
        from tools.py.bn128_field import FQ2
        from tools.py.utils import splitFQP, split
        a = 2 ** 126 - 10

        a2 = FQ2([a, a])

        ids.input= a

        product = a2 * a2

        split_product = splitFQP(product)
        ids.py_res_e0_low, ids.py_res_e0_high  = split_product[0][0], split_product[0][1],
        ids.py_res_e1_low, ids.py_res_e1_high  = split_product[1][0], split_product[1][1]
    %}

    let in = FQ2(Uint256(low=input, high=input), Uint256(low=input, high=input));
    let res: FQ2 = fq2_lib.mul(in, in);

    assert res.e0.low = py_res_e0_low;
    assert res.e0.high = py_res_e0_high;
    assert res.e1.low = py_res_e1_low;
    assert res.e1.high = py_res_e1_high;

    return ();
}