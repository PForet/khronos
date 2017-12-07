from __future__ import absolute_import

from ..utils.catch import catch_array
from ..utils.time_utils import generate_timeline

class series_1d:
    """Data structure for evenly spaced one dimentional time series
    
    Take an array as an input. Optionnaly take arguments to define the dates of
    the observations.
    
    The sampling dates can be supplied as a list (timeline)
    Alternatively, a first and last date of sampling can be given (with `start_date`
    and `end_date`), or a first date and a sampling periode (with `start_date` and `by`)
    If no optionnal argument are given, a start date of 0 and a periode of 1 is assumed
    
    # Arguments:
        values: Numpy Array, the values of the time serie.
        timeline: Array or list, the dates of observation of the values, must be
            the same length as `values`.
        start_date: A date object, the date of the first observation.
        end_date: A date object the date of the last observation.
        by: a time_delta, the periode between each sampling.
    """
    def __init__(self, values,
                 timeline=None,
                 start_date=None,
                 end_date=None,
                 by=None):
        self.values = catch_array(values) #Test for array of length > 1
        self.N = len(values)
        
        if timeline is not None:
            #If a `timeline` was passed, we must sort the values in case `timeline` was not ordered
            if len(timeline)!=len(values): # Raise error if lengths are not consistent
                raise ValueError("Values and timeline should be of the same length")
            #Sort the values and unzip (convert to list to pass futur tests)
            a, b = zip(*sorted(zip(timeline, self.values)))
            self.timeline, self.values = list(a), catch_array(list(b))
        
        elif any(e is not None for e in (start_date, end_date, by)):
            self.timeline, _ = generate_timeline(self.N, start_date, end_date, by)
            
        else: #We must assume the default configuration
            self.timeline = range(self.N)
        
            
        
        
            
