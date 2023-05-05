import 'dart:io';

void main() {
  final n = int.parse(stdin.readLineSync());
  print((n+1)*n ~/ 2);
}
