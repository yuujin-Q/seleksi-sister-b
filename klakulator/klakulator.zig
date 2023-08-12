const std = @import("std");

fn readInteger() !i32 {
    const stdin = std.io.getStdIn().reader();
    const stdout = std.io.getStdOut().writer();

    var buf: [20]u8 = undefined;

    try stdout.print("Input integer : ", .{});

    if (try stdin.readUntilDelimiterOrEof(buf[0..], '\n')) |user_input| {
        var trimmed = std.mem.trimRight(u8, user_input[0..], "\r");
        return std.fmt.parseInt(i32, trimmed, 10);
    } else {
        return @as(i32, 0);
    }
}

fn addition(operand_1: i32, operand_2: i32) i32 {
    var carry: i32 = operand_1 & operand_2;
    var result: i32 = operand_1 ^ operand_2;

    while (carry != 0) {
        var shifted_carry: i32 = carry << 1;
        carry = result & shifted_carry;
        result ^= shifted_carry;
    }
    return result;
}

fn subtraction(operand_1: i32, operand_2: i32) i32 {
    // add operand_1 to negative of operand_2
    return addition(operand_1, addition(~operand_2, 1));
}

fn absoluteValue(operand: i32) i32 {
    var mask: i32 = operand >> 31;
    return addition(mask, operand) ^ mask;
}

fn sign(operand: i32) i32 {
    return (operand >> 31) & 1;
}

fn muldiv(operand_1: i32, operand_2: i32, multiply: bool) i32 {
    const sign_bit: i32 = (sign(operand_1) ^ sign(operand_2));

    var result: i32 = 0;
    const result_increment: i32 = if (multiply) absoluteValue(operand_2) else 1;

    var counter: i32 = absoluteValue(operand_1);
    const counter_decrement: i32 = if (multiply) 1 else absoluteValue(operand_2);

    while (counter >= counter_decrement) {
        counter = subtraction(counter, counter_decrement);
        result = addition(result, result_increment);
    }

    return if (sign_bit == 0) result else subtraction(0, result);
}

fn readExpression() !void {
    const stdout = std.io.getStdOut().writer();
    const stdin = std.io.getStdIn().reader();

    var buf: [20]u8 = undefined;

    try stdout.print("Calculate : \n", .{});

    if (try stdin.readUntilDelimiterOrEof(buf[0..], '\n')) |user_input| {
        var trimmed = std.mem.trimRight(u8, user_input[0..], "\r");
        
        var it = std.mem.split(u8, trimmed[0..], " ");
        while (it.next()) |x| {
            try stdout.print("{s} ", .{x});
        }
    }
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    
    try stdout.print("===========Klak3ulator===========\n", .{});
    try stdout.print("Valid Operators: + - * /\n", .{});
    try stdout.print("Input example: 1 + 2 * 3\n", .{});
    try stdout.print("Note: separate operands and operators using ' ' (single space)\n", .{});
    try stdout.print("Note: operations evaluated from left to right\n", .{});
    
    try readExpression();
}
