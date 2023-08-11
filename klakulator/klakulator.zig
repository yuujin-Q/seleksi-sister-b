const std = @import("std");

fn read_integer() !i32 {
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


pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    var a: i32 = try read_integer();
    try stdout.print("Hello, {d}!\n", .{a});
}