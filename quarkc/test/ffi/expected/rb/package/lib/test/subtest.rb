module Quark
require "quark"
def self.test; Test; end
module Test
def self.subtest; Subtest; end
module Subtest
require 'quark' # .../reflect test/subtest


def self.go()
    
    nil


    nil
end

def self.Test; Test; end
class Test < ::DatawireQuarkCore::QuarkObject
    attr_accessor :size
    extend ::DatawireQuarkCore::Static

    static test_subtest_Test_ref: -> { nil }



    def initialize()
        self.__init_fields__

        nil
    end




    def go()
        
        nil

        nil
    end

    def _getClass()
        
        return "test.subtest.Test"

        nil
    end

    def _getField(name)
        
        if ((name) == ("size"))
            return (self).size
        end
        return nil

        nil
    end

    def _setField(name, value)
        
        if ((name) == ("size"))
            (self).size = ::DatawireQuarkCore.cast(value) { ::Integer }
        end

        nil
    end

    def __init_fields__()
        
        self.size = nil

        nil
    end


end
Test.unlazy_statics


require_relative '../package_md' # 0 () ('test',)

end # module Subtest
end # module Test
end # module Quark
