#coding:utf-8

import zmq
import fire


def init_keepalive(sock):
    sock.setsockopt(zmq.TCP_KEEPALIVE,1)
    sock.setsockopt(zmq.TCP_KEEPALIVE_IDLE,120)
    sock.setsockopt(zmq.TCP_KEEPALIVE_INTVL,1)
    sock.set_hwm(0)

def test_keepalive():
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    init_keepalive(sock)
